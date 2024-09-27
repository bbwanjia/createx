# CREATEX

![Language: Python](https://img.shields.io/github/languages/top/bbwanjia/createx)
![License](https://img.shields.io/github/license/bbwanjia/createx)
![Last commit](https://img.shields.io/github/last-commit/bbwanjia/createx)

[<img src="https://img.shields.io/badge/python%20style-black-000000.svg" alt="Python style: black">](https://github.com/psf/black)
[<img src="https://img.shields.io/badge/types-pyright-00cca7.svg" alt="types: pyright">](https://github.com/PyCQA/pyflakes)
[<img src="https://img.shields.io/badge/lint-pyflakes-ff69b4.svg" alt="lint: pyflakes">](https://github.com/PyCQA/pyflakes)
![Forks](https://img.shields.io/github/forks/bbwanjia/createx)
![Stars](https://img.shields.io/github/stars/bbwanjia/createx)

*An auto* $\TeX$ *file maker*.

## Usage

**CREATEX** can automatically generate templated $\TeX$ files using command line. See commands below.
*Important* The file `settings.py` must be configured before first using it.
You can modify `settingsexample.py` and save it with name `settings.py`.

## Commands

> For simplicity, now you can conveniently create a TEX file using 
> command `create [type of tex] -filepath`. For example, if you want to 
> create a *beamer* named *example*, you type `create beamer example`.

- `create [blank|note|article|beamer] filepath` creates a file using templates. Currently there are  four templates: `blank|note|article|beamer`.
- `edit filepath` opens Vim for editing the file quickly from command prompt.
- `open filepath` opens the file using default application.
- `del filepath` deletes the file under second confirmation.
- `make filepath` complies the file using default `pdflatex` complier. Notice that a $\TeX$ distribution must be installed on the client and it is not included in this program. TeX Live is recommended.
- `show [option]` shows details about warranty and contribution, according to the GNU General Public License version 3.0.

## Further Targets
- Switch to C language
- Compile the program
- more templates
- better machine-independent support
