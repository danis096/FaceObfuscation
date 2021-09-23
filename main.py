# NOTE:
import faceRec
import draw
import gui
import stego

SCALEFACTOR = 1.07

# seed == deterministic number generator seed
def obfuscate(seed, imagePath, outputFolder, operator):
    # returns [[186 290 230 230]] x y w h
    faceCoordinates = faceRec.faceRec(imagePath, SCALEFACTOR)
    outputFolderP = setOutputName(imagePath, outputFolder)
    if len(faceCoordinates) <= 0:
        print(imagePath)
        return 2

    code = draw.obfuscate(seed, imagePath, faceCoordinates, outputFolderP, operator)
    return code


def setOutputName(imPath, outputP):
    # splits path one time, at the end. output is: path/path/path[0] name.png[1]
    nameaux = imPath.rsplit("/", 1)[1]
    # splits name, extracting just name without format
    name = nameaux.split(".")[0]
    # The image output is always .png but this can be changed for another format without aggressive compression like bmp
    output = outputP + "/" + name + "_output.png"
    return output


def handleExitCode(code):
    if code == 0:
        gui.sg.popup('Operation was succesfull!')
        exit()
    elif code == 1:
        gui.sg.popup('Error in execution')
        exit()
    elif code == 2:
        gui.sg.popup('Faces were not Found. Try to modify SCALEFACTOR')
        exit()
    elif code ==4:
        gui.sg.popup('CODE NOT FINISHED YET')
        exit()

def stringToList(faceData):
    faceData = faceData[:-1]
    finalList = []
    rawfaces = faceData.rsplit('|')
    for rawcoords in rawfaces:
        rawcoord = rawcoords.rsplit(' ')
        templist = []
        for coord in rawcoord:
            templist.append(int(coord))
        finalList.append(templist)
    return finalList
# operator = True -> obfuscation process
# operator = False -> reverse process
def manager(seed, imagePath, outputFolder, operator):
    outputFolderP = setOutputName(imagePath, outputFolder)
    #Here we obfuscate the faces found in image
    if operator == True:
        faceCoordinates = faceRec.faceRec(imagePath, SCALEFACTOR)
        # check if faces found in image
        if len(faceCoordinates) <= 0:
            print(imagePath)
            # return code 2, see handleexitcode()
            return 2
        else:
            code, faceData = draw.obfuscate(seed, imagePath, faceCoordinates, outputFolderP, operator)
        if faceData == '':
            return 2
        else:
            # transform facial coordinates into ascii before hide in image
            fdataascii = faceData.encode('ascii')
            # steganography function
            stego.stego_hide(outputFolderP, fdataascii, outputFolderP)
            return 0
        return 0
    # Here we reverse obfuscation of the faces found in image
    elif operator == False:
        faceData = stego.stego_find(imagePath)
        fcextracted = stringToList(faceData)
        if faceData == '':
            return 2
        else:
            code, faceData = draw.obfuscate(seed, imagePath, fcextracted, outputFolderP, operator)
            return 0

def main():
    code = gui.init()
    handleExitCode(code)
    exit()


if __name__ == "__main__":
    main()