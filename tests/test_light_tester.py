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
