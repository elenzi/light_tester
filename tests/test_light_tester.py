 #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `light_tester` package."""


import unittest
import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from light_tester import light_tester
from light_tester import cli
from light_tester import utils

def test_command_line_interface():
    ifile = "/Users/elenalanigan/softeng/data/test.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    
def test_read_file():
    ifile = "/Users/elenalanigan/softeng/data/test.txt" 
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
