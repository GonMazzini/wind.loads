"""Standard library imports"""
import numpy as np  # 1.19.4
import pandas as pd  # 1.2.0
import scipy as sp  # 1.6.0

print(f'numpy version {np.__version__} , \t pandas version {pd.__version__} , \t scipy version {sp.__version__}')


class Rotor():
    """
    Class to represent the wind turbine rotor.

    Attributes
    ----------
    blades_num : int
        number of blades of the rotor.
    radio:
        radio of the rotor.

    Methods
    -------
    lift_drag_coef

    """
