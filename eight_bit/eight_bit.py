from pyxelate import Pyx, Pal
from skimage import io
from skimage.color import rgb2gray
from os.path import split

def eight_bit(image_name):
    """_summary_
    Returns:
        _type_: _description_
    """
    #Load Image
    image = io.imread(image_name)
    #Downfactor and Color Palette
    downfactor = 8
    upscale = 4
    sobel = 2
    palette = Pal.TELETEXT
    #Transformer
    pyx = Pyx(palette = palette, factor = downfactor, upscale = upscale, sobel = sobel, dither = 'bayer')
    #Fit Transform Image
    transformed_image = pyx.fit_transform(image)
    dirname, basename = split(image_name)
    io.imsave(f'{dirname}/new_{basename}', transformed_image)
    #return transformed_image

def to_gray(image_name):
    """_summary_

    Args:
        image_name (_type_): _description_
    """
    image = io.imread(image_name)[:, :, :3]
    #print(type(image))
    transformed_image = rgb2gray(image).astype('uint8')
    dirname, basename = split(image_name)
    io.imsave(f'{dirname}/bw_{basename}', transformed_image)