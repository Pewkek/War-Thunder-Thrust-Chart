import math
import scipy.constants as const
import sympy as sp
from IPython.display import display

ft = 12*0.0254
speed = 242.584961
alt = 9143.441406
alt_ft = alt/ft
tas = 1425
ias = 873

spGasConst = const.gas_constant/28.9647e-3 # specific gas constant = R/dry_air_mol_mass
# troposphere
temp0 = sp.sympify("288.15 - (6.5e-3)*h") # 15 deg - 0.0065 deg every meter
pres0 = sp.sympify("1013.25e2 * (288.15/T)**(g/R/-6.5e-3)") # 15 deg

# tropopause
temp1 = 216.65
pres1 = sp.sympify("22632.05545875171 * exp( (R/216.65) * (11e3-h) )")

# to do: rest

density = sp.sympify("p/(R*T)")

data = {
	"h": alt,
	"R": spGasConst,
	"g": const.g
}

temp = temp1.evalf(subs=data)
data["T"] = temp
pres = pres1.evalf(subs=data)
data["p"] = pres
dens = density.evalf(subs=data)
densSL = 1.225
calculatedTAS = ias*math.sqrt(densSL/dens)
display(calculatedTAS)