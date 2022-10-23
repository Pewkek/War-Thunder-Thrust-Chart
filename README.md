# War Thunder thrust chart generator

![F-4E thrust chart](https://github.com/Pewkek/War-Thunder-Thrust-Chart/raw/master/f4e.png)

#### Special thanks to [gszabi99](https://github.com/gszabi99) for [War Thunder Datamine](https://github.com/gszabi99/War-Thunder-Datamine) repo

## This is a WIP project, uploaded here for ease of sharing

### So, how to get started?
First, we need to grab a flightmodel file, either by datamining ourselves, or using existing resources such as the datamine linked above. We'll use [F-4E](https://raw.githubusercontent.com/gszabi99/War-Thunder-Datamine/master/aces.vromfs.bin_u/gamedata/flightmodels/fm/f-4e.blkx) in this example.  
The Jupyter notebook and flightmodel file must be in the same folder. Inside the .ipynb just change the filename and title accordingly.  
After executing the cell, we should end up with a thrust map, which will also be saved as PNG with filename the same as the graph title.