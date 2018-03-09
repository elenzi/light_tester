import sys
import click
import utils
import led_tester

click.disable_unicode_literals_warning = True
@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input=None):
    """Console script for led_tester."""
    print("input", input)

#     ifile = "/Users/elenalanigan/softeng/data/input_assign3.txt"
    N, instructions = utils.parseFile(input)
    matrix = led_tester.LEDTester(N, instructions)
    #matrix.turnon()#

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover