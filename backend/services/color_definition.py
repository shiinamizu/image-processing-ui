import math
import services.utils as utils
def colorDifine():
    color =0

    return color

def lab2rgbInout(lab):
    L =lab[0]
    a = lab[1]
    b = lab[2]
    RGB = lab2rgb(L,a,b)

    return RGB

def rgb2lab(r,g,b):
    x,y,z = rgb2xyz(r,g,b)
    l,a,b =xyz2lab(x,y,z)
    return l,a,b

def rgb2xyz(r,g,b):
    var_R = ( r / 255 )
    var_G = ( g / 255 )
    var_B = ( b / 255 )

    if ( var_R > 0.04045 ):
        var_R = ( ( var_R + 0.055 ) / 1.055 ) **2.4
    else:
        var_R = var_R / 12.92
    if ( var_G > 0.04045 ) :
        var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_G = var_G / 12.92
    if ( var_B > 0.04045 ):
        var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

    return X,Y,Z

def xyz2lab(x,y,z):

    Reference_X =95
    Reference_Y =100
    Reference_Z =108

    # XYZ (Tristimulus) Reference values of a perfect reflecting diffuser
    var_X = x / Reference_X
    var_Y = y / Reference_Y
    var_Z = z / Reference_Z

    if ( var_X > 0.008856 ):
        var_X = var_X **( 1/3 )
    else:
         var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ):
        var_Y = var_Y ** ( 1/3 )
    else:
         var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ):
        var_Z = var_Z ** ( 1/3 )
    else:
         var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    L = ( 116 * var_Y ) - 16
    a = 500 * ( var_X - var_Y )
    b = 200 * ( var_Y - var_Z )

    return L,a,b     

def lab2rgb(L,a,b):
    d = 6 / 29
    fy = (L + 16) / 116
    fx = fy + a / 500
    fz = fy - b / 200
    
    if(fy > d):
        Y = fy*fy*fy
    else:
        Y = (fy - 16 / 116) * 3 * d * d
    if (fx > d):
        X = fx * fx * fx
    else:
        X = (fx - 16 / 116) * 3 * d * d
    if(fz > d):
        Z = fz * fz * fz
    else:
        Z =(fz - 16 / 116) * 3 * d * d
    X *= 95.047
    Y *= 100.0
    Z *= 108.883
    R = 3.2406 * X + (-1.5372) * Y + (-0.4986) * Z
    G = (-0.9689) * X + 1.8758 * Y + 0.0415 * Z
    B = 0.0557 * X + (-0.2040) * Y + 1.0570 * Z
    RGB = [R, G, B]
    for i in range(3):
        v = RGB[i] / 100
        if (v > 0.0405 / 12.92):
            v = math.pow(v, 1 / 2.4)
            v *= 1.055
            v -= 0.055
        else: 
            v *= 12.92
        RGB[i] = round(v * 255)
    return RGB

def isEqual(c1,c2):
    for i in range(len(c1)):
        if (c1[i]!=c2[i]):
            return False
    return True

def labBoundary(pin,pout):
    mid =[]
    for i in range(len(pin)):
        m = (pin[i]+pout[i])/2
        mid.append(m)

    RGBin =lab2rgbInout(pin)
    RGBout =lab2rgbInout(pout)
    RGBmid =lab2rgbInout(mid)

    if ( (utils.distance2(pin,pout)<0.001 )or (isEqual(RGBin,RGBout))):
        return mid
    if (isOutRGB(RGBmid)):
        return labBoundary(pin,mid)
    else:
        return labBoundary(mid,pout)


    
def cliping(RGB):
    for i in range(3):
        if ( (RGB[i]<0)):
            RGB[i]=0
        elif (RGB[i]>255):
            RGB[i]=255
    return RGB

def isOutRGB(RGB):
    for i in range(3):
        if ( (RGB[i]<0) or (RGB[i]>255) ):
            return True
    
    return False
    
def isOutLab(lab):
    return isOutRGB(lab2rgbInout(lab))

def labIntersect(p1,p2):
    if(isOutLab(p2)):
        return labBoundary(p1,p2)
    else:
        return labIntersect(p2,utils.add(p2,utils.sub(p2,p1)))



