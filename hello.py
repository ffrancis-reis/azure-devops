import click


@click.command(help="This is just a hello app. It does nothing!")
@click.option("--name", prompt="I need your name", help="Needa name")
@click.option("--color", prompt="I need your color", help="this is your")
def hello(name, color):
    if name == "Thor":
        click.echo("Thor your are always red")
        click.echo(click.style(f"Hello World! {name}", fg="red"))
    else:
        click.echo(f"Your color is {color}!")
        click.echo(click.style(f"Hello {name}!", fg=color))


if __name__ == "__main__":
    hello()


def add(x, y):
    return x+y


def test_add():
    total = add(1, 2)
    assert total == 3
