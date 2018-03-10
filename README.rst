============
light_tester
============


.. image:: https://img.shields.io/pypi/v/light_tester.svg
        :target: https://pypi.python.org/pypi/light_tester

.. image:: https://img.shields.io/travis/elenzi/light_tester.svg
        :target: https://travis-ci.org/elenzi/light_tester

.. image:: https://readthedocs.org/projects/light-tester/badge/?version=latest
        :target: https://light-tester.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status





Features
--------

The board is a square grid of LEDs which we control by sending commands to the unit
to turn on or off certain rectangular regions.

The L × L lights can be modelled as a 2 dimensional grid with L rows of lights and L
lights in each row and the LED's at each corner are (0, 0), (0, L − 1), (L − 1, L − 1)
and (L − 1, 0).

The lights are either on or off.

This application's job is to test the lights. 



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
