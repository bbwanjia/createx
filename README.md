# CREATEX

Create a LaTeX file from a template with a short command. Python 3 is required; compiling requires a separate TeX installation with `pdflatex`.

## Setup

Clone the project, then copy `settingsexample.py` to `settings.py` and edit the author, date, header, footer, and Beamer theme values as needed. If `settings.py` is absent, the example values are used. The template directory is found relative to the program, so `abspath` in older settings files is no longer needed.

Run the scripts from the project directory, or put the directory on your `PATH`:

```sh
./create article paper
./createx create beamer slides.tex
```

Both examples create a `.tex` file in the current directory. A `.tex` extension is added when omitted. Quote paths that contain spaces, for example `./create report "project report"`. Existing files are never overwritten.

## Commands

| Command | Action |
| --- | --- |
| `create TYPE filepath` | Create a file from the named template. The `create` script is a shortcut for this command: `./create TYPE filepath`. |
| `edit filepath` | Open the file in Vim. |
| `open filepath` | Open the file with the system's default application. |
| `del filepath` | Delete the file after you type its exact filename, including `.tex`. |
| `make filepath` | Compile the file with `pdflatex`. |
| `show w` / `show c` | Show warranty or contribution information. |
| `help` | Show command help. |
| `quit` | Leave the interactive prompt. |

Use `./createx` with no arguments for the interactive prompt. You can also pass a command directly, such as `./createx help` or `./createx make paper`. Commands and their arguments are unchanged; invalid or incomplete commands now report an error. Interactive input supports quoted paths.

## Templates

| Type | Starting point |
| --- | --- |
| `blank` | Basic article structure and theorem environments. |
| `article` | Article with mathematics and theorem environments. |
| `beamer` | Presentation with a title slide and section outline. |
| `note` | Notes with configurable page headers and footer. |
| `book` | Book with chapter formatting and a contents page. |
| `report` | Report with title, contents, and chapter headings. |
| `letter` | Formal letter with an opening and closing. |
| `homework` | Problem and solution layout for assignments. |

The first five templates are the project's original template files. The three new templates are separate files. Generated files replace the template's title, author, date, header, footer, and theme markers with configured values. Filename characters that have special meaning in LaTeX are escaped in generated titles. The original blank template also receives `article` as its document class, and empty content markers become editable space.

## Checking the project

Run `python3 -m unittest test_createx.py` to check parsing, file creation, and deletion behavior. `pdflatex` is only needed for compiling generated files.

Licensed under the GNU General Public License, version 3 or later; see [LICENSE](LICENSE).
