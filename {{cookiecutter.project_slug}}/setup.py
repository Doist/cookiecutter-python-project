import io
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


with io.open(os.path.join(here, "README.md"), "rt") as f:
    long_description = "\n" + f.read()

version_mod = {}
with open(os.path.join(here, "{{ cookiecutter.root_package }}", "__version__.py")) as f:
    exec(f.read(), version_mod)

setup(
    name="{{ cookiecutter.project_slug }}",
    version=version_mod["__version__"],
    packages=find_packages(exclude=["tests"]),
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    license="{{ cookiecutter.project_license }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    install_requires=[],
    # see here for complete list of classifiers
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Intended Audience :: Developers",
        {% if cookiecutter.project_license == 'Proprietary' -%}
        "License :: Other/Proprietary License",
        "Private :: Do Not Upload",
        {% else -%}
        "License :: OSI Approved :: {{ cookiecutter.project_license }} License",
        {% endif -%}
        "Programming Language :: Python",
    ],
)
