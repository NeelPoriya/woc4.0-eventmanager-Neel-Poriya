# Run the program and compress your image file, without losing any quality.

import PIL
from PIL import Image
from tkinter.filedialog import *
img = Image.open(askopenfilename())
img = img.resize(img.size, Image.ANTIALIAS)
img.save(asksaveasfilename()+".jpg")
