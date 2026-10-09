import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from action import Action, CommandError
from base import TEX_TYPES
from main import run
from parse import Ocreate, Odel, Omake


class CommandTests(unittest.TestCase):
    def test_command_shapes(self):
        for words in (["create"], ["create", "article"], ["show"], ["edit"], ["help", "extra"], ["create", "missing", "file"]):
            with self.subTest(words=words), self.assertRaises(CommandError):
                Action(words)

    def test_path_and_title(self):
        action = Action(["create", "article", "a directory/my paper.tex"])
        self.assertEqual(action.title, "my paper")
        self.assertTrue(action.path.endswith("a directory/my paper.tex"))

    def test_every_template_generates_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            for template in TEX_TYPES:
                with self.subTest(template=template):
                    target = Path(directory) / f"{template}.tex"
                    with patch("sys.stdout", new_callable=io.StringIO):
                        self.assertEqual(Ocreate(template, str(target), template), 0)
                        self.assertEqual(Ocreate(template, str(target), template), 1)
                    content = target.read_text(encoding="utf-8")
                    self.assertIn("\\begin{document}", content)
                    self.assertNotIn("**", content)

    def test_title_escapes_latex_characters(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "draft_notes.tex"
            with patch("sys.stdout", new_callable=io.StringIO):
                self.assertEqual(Ocreate("article", str(target), "draft_notes"), 0)
            self.assertIn(r"draft\_notes", target.read_text(encoding="utf-8"))

    def test_delete_requires_exact_filename(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "sample.tex"
            target.write_text("keep", encoding="utf-8")
            with patch("builtins.input", return_value=""), patch("sys.stdout", new_callable=io.StringIO):
                self.assertEqual(Odel(str(target)), 1)
            self.assertTrue(target.exists())
            with patch("builtins.input", return_value="sample.tex"), patch("sys.stdout", new_callable=io.StringIO):
                self.assertEqual(Odel(str(target)), 0)
            self.assertFalse(target.exists())

    def test_invalid_command_returns_failure(self):
        with patch("sys.stdout", new_callable=io.StringIO):
            self.assertEqual(run(["create", "article"]), 1)

    def test_make_passes_path_as_one_argument(self):
        with patch("parse.subprocess.run") as process:
            process.return_value.returncode = 0
            self.assertEqual(Omake("/tmp/a file;name.tex"), 0)
            process.assert_called_once_with(
                ["pdflatex", "/tmp/a file;name.tex"], check=False
            )


if __name__ == "__main__":
    unittest.main()
