from __future__ import print_function

VERSION = {{cookiecutter.project_version_tuple}}
__version__ = ".".join(map(str, VERSION))

if __name__ == "__main__":
    print(__version__)
