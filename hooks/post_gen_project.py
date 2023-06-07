#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove a given file from the project directory."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_directory(dirpath: str) -> None:
    """Remove a given directory from the project directory."""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))

if __name__ == "__main__":

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.__project_name }}", "cli.py")
        remove_file(cli_file)

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")

    if "{{ cookiecutter.create_dot_github_directory }}" == "n":
        remove_directory(".github")

    if "{{ cookiecutter.create_tests_directory }}" == "n":
        remove_directory("tests")
