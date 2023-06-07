import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_name = '{{ cookiecutter.project_name}}'
module_name = '{{ cookiecutter.__project_name}}'

if not re.match(MODULE_REGEX, module_name):
    print(f"ERROR: The given project name was: {project_name}, which gives the module name: {module_name}")
    print(f"ERROR: This module name ({module_name}) is not a valid Python module name.")
    print(f"It must match the regular expression: {MODULE_REGEX}")

    # Exit to cancel project
    sys.exit(1)
