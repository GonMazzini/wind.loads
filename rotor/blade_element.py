"""1 Standard library imports"""
import numpy as np  # 1.19.4
import pandas as pd  # 1.2.0
import scipy as sp  # 1.6.0
from scipy.interpolate import interp1d

print(f'numpy version {np.__version__} , \t pandas version {pd.__version__} , \t scipy version {sp.__version__}')


class Rotor:
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
    lift_drag_coeff

    """

    """Load the aerodynamics profile for DTU 10 MW"""

    ffa_241 = pd.read_csv('FFA-W3-241.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_301 = pd.read_csv('FFA-W3-301.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_360 = pd.read_csv('FFA-W3-360.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_480 = pd.read_csv('FFA-W3-480.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    ffa_600 = pd.read_csv('FFA-W3-600.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])
    cylinder = pd.read_csv('cylinder.txt', sep='\t', names=['alpha', 'Cl', 'Cd', 'Cm'])

    ffa_dict = dict(zip(np.arange(6), [ffa_241, ffa_301, ffa_360, ffa_480, ffa_600, cylinder]))

    # load the blade data.
    blade_data = pd.read_csv('bladedat.txt', sep='\t', names=['r', 'twist', 'c', 't/c'])

    def __init__(self, blades_num=3, radio=89.17):
        self.blades_num = blades_num
        self.radio = radio

    @staticmethod  # d oes not use self in its body and hence does not actually change the class instance.
    # Hence the method could be static, i.e. callable without passing a class instance or without even having
    # created a class instance.
    def lift_drag_coefficient(alpha, t_c):
        """Interpolation for drag and lift coefficients.

         Returns: (Cl, Cd)

         --------------parameters:

         t_c: float (ie. 24.1)
         alpha: int or float (rad)
         """
        # vectors for cd and cl for each thickness
        cdthick, clthick = np.zeros(6), np.zeros(6)

        for k in range(6):
            f1cl = interp1d(Rotor.ffa_dict[k].iloc[:, 0], Rotor.ffa_dict[k].iloc[:, 1])
            f1cd = interp1d(Rotor.ffa_dict[k].iloc[:, 0], Rotor.ffa_dict[k].iloc[:, 2])
            clthick[k] = f1cl(alpha * 180 / np.pi)  # must convert into degrees
            cdthick[k] = f1cd(alpha * 180 / np.pi)

        thick_ratio = np.array([24.1, 30.1, 36., 48., 60., 100.])
        f2cl = interp1d(thick_ratio, clthick)
        f2cd = interp1d(thick_ratio, cdthick)
        cl = f2cl(t_c)
        cd = f2cd(t_c)

        return cl, cd


if __name__ == '__main__':
    wt = Rotor()
    print(wt.radio)
    print('finish ran blade_element')
    Rotor.lift_drag_coefficient(alpha=0, t_c=24.1)
