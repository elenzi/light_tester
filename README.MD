===========
lighttester
===========


Light tester for Science Centre.




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
