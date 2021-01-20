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
    def __init__(self, blades_num=3, radio=89.17):
        self.blades_num=blades_num
        self.radio=radio

    """Load the aerodynamics profile for DTU 10 MW"""

    ffa_241 = pd.read_csv('FFA-W3-241.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_301 = pd.read_csv('FFA-W3-301.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_360 = pd.read_csv('FFA-W3-360.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_480 = pd.read_csv('FFA-W3-480.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_600 = pd.read_csv('FFA-W3-600.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    cylinder = pd.read_csv('cylinder.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])


