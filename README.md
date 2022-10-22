# War Thunder thrust chart generator

![F-4E thrust chart](https://github.com/Pewkek/War-Thunder-Thrust-Chart/raw/master/f4e.png)

#### Special thanks to [gszabi99](https://github.com/gszabi99) for [War Thunder Datamine](https://github.com/gszabi99/War-Thunder-Datamine) repo

## This is a WIP project, uploaded here for ease of sharing

### So, how to get started?
First, we need to grab a flightmodel file, either by datamining ourselves, or using existing resources such as the datamine linked above

In this example we'll use US [F-4E](https://github.com/gszabi99/War-Thunder-Datamine/blob/master/aces.vromfs.bin_u/gamedata/flightmodels/fm/f-4e.blkx) file. Version used to make above graph is included in this repo.

Inside the file itself we need to scroll into EngineType area and grab a few values, mainly:
* AfterburnerBoost from section Main
* Altitudes from section ThrustMax, they need to be rewritten into the script (currently)
* Velocities from section ThrustMax, they also need to be rewritten (currently)
* ThrustMax0 from section Main
* Thrust coefficients excluding ThrustMax0 (so everything below it all the way to the closing bracket, excluding the bracket itself, take a look at the .ipynb)
* Multipliers for 100% and 110% (WEP) throttle, which are just under thrust coefficients, listed inside Mode# where # is some number. We take the value ThrustMult from the modes that have Throttle listed as 1.0 (100%) and 1.1 (110% which is WEP).

having above values, we replace them inside the example .ipynb file and we should end up with two 3D thrust graphs.

There are more variables that can be changed, but more information is listed inside the example .ipynb itself.