import pkg_resources

__version__ = pkg_resources.get_distribution("{{ cookiecutter.project_slug }}").version
