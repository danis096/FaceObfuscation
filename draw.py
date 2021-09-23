from PIL import Image
import random


def obfuscate(seed, image, fcoordinates, outputf, operator):
    """

    :param seed: indicates random number generator
    :type seed: str | int
    :param image: image to be processed
    :type image: image
    :param fcoordinates: all coordinates of faces found in the previous image. init X,Y coordinates, and the length
    :type fcoordinates: list
    :param outputf: output path for the result
    :type outputf: string
    :param operator: boolean that indicates if the operation is obfuscate (True) or recover original (False)
    :type operator: True | False
    """
    # define seed
    random.seed(seed)
    # save coordinates of faces founded on image
    fdata = ''
    # print('COORDENADAS', fcoordinates)

    with Image.open(image) as im:
        px = im.load()

        # Face loop
        for (x, y, w, h) in fcoordinates:

            #fdata = fdata + ' ' + ' '.join([str(x), str(y), str(w), str(h)])
            fdata = fdata + '|' + ' '.join([str(x), str(y), str(w), str(h)])
            # X and Y are -> class 'numpy.int32'
            # so we changing them to -> class 'int'. Native python types
            if not isinstance(x, int) or not isinstance(y, int):
                x = x.item()
                y = y.item()
            # print(x, y, w, h)
            # drawing loop
            for j in range(w):
                for i in range(h):
                    # check if we are on even pixel
                    even = True if j % 2 == 0 else False
                    # print('LOS TIPOS DE VARIABLE SON: ', type(x), type(y), type(x1), type(y1))
                    pixel = (x + j, y + i)
                    # print('Coordenadas de pixel son:', pixel)
                    # read pixel data
                    pixData = px[x + j, y + i]
                    #print(pixData)
                    r, g, b = pixData[0], pixData[1], pixData[2]
                    r, g, b, randstate = paintAlg(r, g, b, extractorsum(even, operator), random.getstate())
                    # we recover the random seed state
                    random.setstate(randstate)
                    # Border treatment of pixels 0 < pixel <= 255
                    r, g, b = pixLimits(r, g, b)

                    # print('AFTER: ', r, g, b)
                    im.putpixel(pixel, (r, g, b))
            #print('COORDENADAS CARA: ', x, y, w, h)

        fdata = fdata[1:]
        fdata += '\0'
        #print(fdata)
        #print("Acabo bien aparentemente")
        #im.show()
        im.save(outputf)
        # print('COORDENADAS', fcoordinates)
        #print(type(fcoordinates))
        return 0, fdata


def defSeed(seed):
    random.seed(seed)
    a = []
    for i in range(100):
        if i <= 9:
            a.append(random.randint(10, 20))
        elif 9 < i <= 20:
            a.append(random.randint(21, 50))
        elif 20 < i <= 30:
            a.append(random.randint(51, 70))
        elif 30 < i <= 80:
            a.append(random.randint(71, 120))
        elif 80 < i <= 90:
            a.append(random.randint(121, 150))
        if i > 90:
            a.append(random.randint(151, 170))
    random.shuffle(a)
    # print(random.choice(a))
    # print(random.choice(a))
    # print(random.choice(a))
    # print(a)
    # print(len(a))
    return a


def pixLimits(r, g, b):
    if r < 0:
        r = r + 256
    elif r > 255:
        r = r - 256
    if g < 0:
        g = g + 256
    elif g > 255:
        g = g - 256
    if b < 0:
        b = b + 256
    elif b > 255:
        b = b - 256
    return r, g, b


def extractorsum(even, operator):
    if even is False and operator is False:
        return True
    else:
        return even and operator


def paintAlg(r, g, b, sum, randstate):
    random.setstate(randstate)
    #a = defSeed()
    if sum:
        r = r + random.randint(30, 130)
        g = g + random.randint(30, 130)
        b = b + random.randint(30, 130)
    else:
        r = r - random.randint(30, 130)
        g = g - random.randint(30, 130)
        b = b - random.randint(30, 130)
    return r, g, b, random.getstate()
