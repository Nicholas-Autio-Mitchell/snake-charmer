"""CLI entrypoint for {{cookiecutter.__project_name}}."""

{%- if cookiecutter.command_line_interface|lower == 'hydra' %}
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path=None)
def my_app(cfg: DictConfig) -> None:
    """CLI entrypoint for {{cookiecutter.__project_name}}."""
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse


def main() -> None:
    """CLI entrypoint for {{cookiecutter.__project_name}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument("int_arg", metavar="N", type=int, nargs="+", help="one or more integers")
    args = parser.parse_args()
    print("Arguments: " + str(args._))


if __name__ == "__main__":
    main()
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click


@click.command()
@click.option("--count", default=1, type=int, help="Number of greetings.")
@click.option("--first-name", prompt="Your name", help="First name of the person to greet.")
@click.option("--last-name", prompt="Your name", help="Last name of the person to greet.")
def hello(count: int, first_name: str, last_name: str) -> None:
    """CLI entrypoint for {{cookiecutter.__project_name}}."""
    click.echo("See click documentation at https://click.palletsprojects.com/")
    for _ in range(count):
        click.echo(f"Hello {first_name} {last_name}!")

if __name__ == "__main__":
    hello() # type: ignore
{%- endif %}
