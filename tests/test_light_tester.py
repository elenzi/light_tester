"""Tests for `led_tester` package."""
import sys
sys.path.append('.')
import pytest

from light_tester import utils
from light_tester import led_tester


def test_command_line_interface():
    ifile = "/Users/elenalanigan/softeng/data/test.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    
    
def test_read_file():
    ifile = "/Users/elenalanigan/softeng/data/test.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7']
    
   
def test_read_http():
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 1000
    assert instructions is not None
    
    def test_turn_on(self):
        ifile = "/Users/elenalanigan/softeng/data/test.txt"
        N, instructions = utils.parseFile(ifile)
        assert N is not None
        assert instructions is not None

    def test_turn_off(self):
        ifile = "/Users/elenalanigan/softeng/data/test.txt""
        N, instructions = utils.parseFile(ifile)
        assert N is not None
        assert instructions is not None

    def test_switch(self):
        ifile = "/Users/elenalanigan/softeng/data/test.txt""
        N, instructions = utils.parseFile(ifile)
        assert N is not None
        assert instructions is not None
        
        
