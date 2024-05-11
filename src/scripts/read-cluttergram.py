from PIL import Image
import numpy as np

sims = np.fromfile("./s_01294501_sim.img" , dtype = np.float32)

# Always 3600 samples per col , three cluttergrams ( left , right , combined )
# in each file
ncol = len(sims) // 3600 // 3

leftSim = sims [: len(sims) // 3].reshape((3600 , ncol))
rightSim = sims [ len(sims) // 3 : 2 * len(sims) // 3].reshape((3600 , ncol))
comboSim = sims [2 * len(sims) // 3 :].reshape((3600 , ncol))
# Scale each sim for display and save
for name , sim in [
	("left" , leftSim),
	("right" , rightSim),
	("combo" , comboSim),
]:
	# Log scale image
	simScale = np.log10(sim + 1e-30)
	# Get valid ( actually simulated ) values
	simValid = simScale[sim != 0]
	# Make linear mapping from image values to 0 -255
	p10 = np.percentile(simValid , 10)
	m = 255 / (simValid.max() - p10)
	b = -p10 * m
	# Apply map , clip values below minimum
	simMap = (m * simScale) + b
	simMap[simMap < 0] = 0
	# Save browse image
	simMap = simMap.astype(np.uint8)
	simImg = Image.fromarray(simMap)
	simImg.save("s_01294501_%s.png" % name)