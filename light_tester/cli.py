# -*- coding: utf-8 -*-

"""Console script for light_tester."""
import sys
import click


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input)
    return main(input)


if __name__ == "__main__":
    sys.exit(main())
