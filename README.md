# Starter Template for Python projects at Doist

Use this cookiecutter template 🍪 to start every new Python project at Doist.

## Getting Started

Nothing can be easier:

```
git clone https://github.com/Doist/cookiecutter-python-project.git
cookiecutter cookiecutter-python-project/
```

For Windows, you might need to run `python -m cookiecutter` as the command might not work even though it's correctly configured on the PATH.

## What's inside

The template covers your back with the following elements:

- README.md with a pre-defined structure.
- CHANGELOG.md file with an initial message.
- Stub project template.
- Test directory with a sample test file.
- GitHub workflow configuration to run pytest automatically.
- Pre-configured mypy, Flake8, isort.
- A set of pre-commit hooks.
- pyproject.toml for Poetry.

## How to use it

Before creating a project:

- Install [Poetry](https://python-poetry.org/docs/#installation)
- Choose a project name. Likely, in the format `foo-bar` and create a GitHub
  repository for it. The root package of your project will have a default
  name `foo_bar`. Make sure that you made the repository private if you plan to create
  a private (non-open-source) project.
- Choose the license. For public projects use MIT, for private projects use
  "Proprietary".

After creating a project:

- Initialize git repo with `git init`
- Initialize your pre-commit hooks inside the repo with `pre-commit install`. For
  more details follow https://pre-commit.com/
- Initialize virtual environment and install all dependencies with `poetry install`
- Add all files to the repo, review staged changes and commit them.
- Deploy changes to GitHub.
- For Windows, you might need to change your personal access token to GitHub, see information [here](https://github.com/gitextensions/gitextensions/issues/4916#issuecomment-557509451)

Other hints:

- Use [How to Write Good Documentation](https://www.sohamkamani.com/blog/how-to-write-good-documentation/)
  to fill in our README with the content.
- Use [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) guideline for your
  changelog entries.
  
## How to configure VSCode

At the moment, VSCode doesn't automatically detect Poetry environments. You can set it 
manually though. For a newly created project, create a `.vscode/settings.json`

```
mkdir -p .vscode
cat <<EOF > .vscode/settings.json
{
  "python.pythonPath": "$(poetry env info -p)/bin/python"
}
EOF
```

Ref: https://github.com/microsoft/vscode-python/issues/8372

## How to contribute

Well, just create an issue or a pull request.
