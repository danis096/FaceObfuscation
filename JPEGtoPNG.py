import sys
import draw
import faceRec
import main
import os
from PIL import Image

def file_command(filepath, filename):
    ffilename = filename.rsplit(".", 1)[0]
    ffilename = ffilename + '.png'
    #OUTPUT DIRECTORY
    b_directory = "/home/danis/Escritorio/70morepng"
    im1 = Image.open(filepath)
    outputpath = os.path.join(b_directory, ffilename)
    im1.save(outputpath)
    im1.close()

# INPUT DIRECTORY where files are located
a_directory = "/home/danis/Escritorio/70more"

for filename in os.listdir(a_directory):
    filepath = os.path.join(a_directory, filename)
    file_command(filepath, filename)
