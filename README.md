# CREATEX

*An auto $\LaTeX$ file generator*

## Usage

**CREATEX** can automatically generate templated $\LaTeX$ files using command line. See commands below.
*Important* The file `settings.py` must be configured before first using it.

## Commands

> For simplicity, now you can conveniently create a TEX file using 
> command `create [type of tex] -filepath`. For example, if you want to 
> create a *beamer* named *example*, you type `create beamer example`.

- `create [blank|note|article|beamer] filepath` creates a file using templates. Currently there are  four templates: `blank|note|article|beamer`.
- `edit filepath` opens Vim for editing the file quickly from command prompt.
- `open filepath` opens the file using default application.
- `del filepath` deletes the file under second confirmation.
- `make filepath` complies the file using default $\LaTeX$ complier. Notice that a $\LaTeX$ distribution must be installed on the client and it is not included in this program. TeX Live is recommended.

## Contact the owner of this repository!

Email: `bbwanjia2860@gmail.com`

