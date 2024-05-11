from PIL import Image
import numpy as np

emap = np.fromfile("./s_01294501_emap.img", dtype = np.float32)

# Always 181 rows
ncol = len(emap) // 181

emap = emap.reshape((181 , ncol))

# Log scaling for display
emap = np.log10(emap)
p10 , p99 = np.percentile(emap , (10 , 99))
# Make linear mapping from image values to 0 -255
m = 255 / (p99 - p10)
b = -p10 * m
# Apply map , clip values below min and above max
echoMap = (m * emap) + b
echoMap[echoMap < 0] = 0
echoMap[echoMap > 255] = 255
# Save browse image
echoMap = echoMap.astype(np.uint8)
echoImg = Image.fromarray(echoMap)
echoImg.save("s_01294501_emap.png")