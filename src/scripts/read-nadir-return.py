from PIL import Image
import numpy as np
import pandas as pd

# Read in nadir and first return
rtrn = pd.read_csv("./s_01294501_rtrn.csv", index_col=0)

# Read in sim
sims = np.fromfile("./s_01294501_sim.img" , dtype = np.float32)

# Unpack clutter simulation data
# Always 3600 samples per col , three cluttergrams ( left , right , combined )
# in each file
ncol = len(sims) // 3600 // 3

comboSim = sims[2 * len(sims) // 3 :].reshape((3600 , ncol))

# Log scale combined sim for display
comboScale = np.log10(comboSim + 1e-30)

# Get valid ( actually simulated ) values
comboValid = comboScale[comboSim != 0]

# Make linear mapping from image values to 0 -255
p10 = np.percentile(comboValid , 10)
m = 255 / (comboValid.max() - p10)
b = -p10 * m

# Apply map , clip values below minimum
comboMap = (m * comboScale) + b
comboMap [comboMap < 0] = 0

# Color to draw first return and nadir return location with
firstColor = [255 , 0 , 255]
nadirColor = [50 , 200 , 200]

# Stack sim and data to make RGB image
comboMap = np.dstack((comboMap , comboMap , comboMap)).astype(np.uint8)

# Loop over columns and change color of nadir and first return samples
for i , row in rtrn.iterrows():
	nadirSamp = int(row["NadirLine"])
	firstSamp = int(row["FirstLine"])
	# Color nadir
	comboMap[ nadirSamp , i - 1] = nadirColor
	# Color first return
	comboMap[firstSamp , i - 1] = firstColor

comboImg = Image.fromarray(comboMap)
comboImg = comboImg.convert("RGB")
comboImg.save("s_01294501_rtrn_combo.png")