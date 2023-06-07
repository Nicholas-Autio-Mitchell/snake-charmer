# Contributing

Contributions are welcome and greatly appreciated! Every little helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs to the [issues section](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name }}/issues).

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an [issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name }}/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome.

## Get Started!

Ready to contribute? Here's how to set up `{{ cookiecutter.__project_name }}` for local development.

1. Fork the `{{ cookiecutter.__project_name }}` repo on GitHub.
2. Clone your fork locally:

    ```bash
    $ git clone git@github.com:your_name_here/{{ cookiecutter.__project_name }}.git
    ```

3. Create the development virtual environment:

    ```bash
    $ conda create -n {{ cookiecutter.__project_name }} python={{ cookiecutter.python_version }}
    $ conda activate {{ cookiecutter.__project_name }}
    $ conda install --file requirements-dev.txt
    ```

4. Create a branch for local development::

    ```bash
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

5. Once finished with your changes (and hopefully adding some unit tests :), the pre-commit hooks will run several checks. Fix any reported errors until your commit is accepted.

    ```bash
    $ git commit -am "Description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

    CI will now also run on your commit. Fix any reported errors and repeat previous steps until your commit is accepted.

6.  You can now open the pull request! 👏


## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include a description of the changes and how the changes were tested to be correct.
2. If the pull request adds functionality, the docs should be updated. For example, by adding
   new functionality into a new function with a docstring. Then add the feature to the list in `HISTORY.md`.
