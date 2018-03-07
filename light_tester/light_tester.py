"""Console script for led_tester."""
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

    N, instructions = utils.parseFile(input)

    ledTester = led_tester.LEDtester(N)

    for instruction in instructions:
        ledTester.apply(instruction)

    print('#occupied: ', ledTester.countOccupied()) 
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover