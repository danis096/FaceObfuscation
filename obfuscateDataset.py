import sys

import draw
import faceRec
import main
import os

def file_command(filepath):
    #print(filepath)
    main.obfuscate('ccc', filepath, '/home/danis/Escritorio/obfuscatedsamples2/', True)


a_directory = "/home/danis/Escritorio/rawdataset/datasetpng"

for filename in os.listdir(a_directory):

    filepath = os.path.join(a_directory, filename)

    file_command(filepath)
