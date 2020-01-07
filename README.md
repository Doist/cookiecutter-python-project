# Starter Template for Python projects at Doist

Use this cookiecutter template 🍪 to start every new Python project at Doist.

## Getting Started

Nothing can be easier:

```
git clone https://github.com/Doist/cookiecutter-python.git
cookiecutter cookiecutter-python/
```

## What's inside

The template covers your back with the following elements:

- README.md with a pre-defined structure.
- CHANGELOG.md file with an initial message.
- Stub project template with a version file.
- Test directory with a sample test file.
- Tox configuration to run tests in different environments.
- GitHub workflow configuration to run tox tests automatically.
- Pre-configured mypy, Flake8, isort.
- A set of pre-commit hooks.
- Makefile to build and release new versions of packages.
- Basic setup.py which automatically copies the long description from README.md and
  takes the version from the version file.

## How to use it

Before creating a project:

- Choose a project name. Likely, in the format `doist-foo-bar` and create a GitHub
  repository for it. The root package of your project will have a default
  name `foo_bar`. Make sure that you made the repository private if you plan to create
  a private (non-open-source) project.
- Choose the license. For public projects use MIT, for private projects use
  "Proprietary".

After creating a project:

- Initialize git repo with `git init`
- Initialize your pre-commit hooks inside the repo with `pre-commit init`. For
  more details follow https://pre-commit.com/
- Add all files to the repo, review staged changes and commit them.
- Deploy changes to GitHub.

Other hints:

- Use [How to Write Good Documentation](https://www.sohamkamani.com/blog/how-to-write-good-documentation/)
  to fill in our README with the content.
- Use [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) guideline for your
  changelog entries.

## How to contribute

Well, just create an issue or a pull request.
