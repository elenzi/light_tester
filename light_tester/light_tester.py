import sys
import click
from light_tester import utils
from light_tester import led_tester

click.disable_unicode_literals_warning = True
@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input=None):
    print("input", input)

#     ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = utils.parseFile(input)
    matrix = led_tester.LEDTester(N, instructions)

if __name__ == "__main__":
    sys.exit(main())  