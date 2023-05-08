# jupyter-reorder-python-imports

[reorder-python-imports](https://github.com/asottile/reorder-python-imports) is a great library. Now availble in Jupyter notebook and lab.

## What does it do?
Once loaded, automatically format python imports according to reorder-python-imports using their [formatting methods](https://github.com/asottile/reorder-python-imports#what-does-it-do).

## Quickstart
`python -m pip install jupyter-reorder-python-imports`

Import into Jupyter using two methods:
```
%load_ext jupyter_reorder_python_imports
```
Or,
```
import jupyter_reorder_python_imports

jupyter_reorder_python_imports.load()
```
The latter method allows for specifying the minimum python version (as a tuple of integers) to be used for [removing obsolete `__future__` imports](https://github.com/asottile/reorder-python-imports#removing-obsolete-__future__-imports). For example, `jupyter_reorder_python_imports.load(min_python_version=(3,9))` specifies 3.9 as the minimum python version.

## TODO
Contribution ideas:
- [ ] Improve testing

## Acknowledgements
Of course, thanks to the [reorder-python-imports](https://github.com/asottile/reorder-python-imports) and [jupyter](https://jupyter.org/) teams for their continued work that we all use!

Further, thanks to [jupyter-black](https://github.com/n8henrie/jupyter-black) whose code greatly helped this project.
