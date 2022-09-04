import os
from pyxelate import Pyx, Pal
from skimage import io
from skimage.color import rgb2gray

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
    #Fit and Transform Image
    transformed_image = pyx.fit_transform(image)
    dirname, basename = os.path.split(image_name)
    io.imsave(f'{dirname}/new_{basename}', transformed_image)
    #return transformed_image

def to_gray(image_name):
    """_summary_

    Args:
        image_name (_type_): _description_
    """
    image = io.imread(image_name)[:, :, :3]
    transformed_image = rgb2gray(image).astype('uint8')
    dirname, basename = os.path.split(image_name)
    io.imsave(f'{dirname}/bw_{basename}', transformed_image)

def get_file_names(
    path,
    file_types = ['jpeg', 'jpg', 'png']
    ):
    """
    Devuelve una lista con los archivos de los tipos dados
    Args:
        path (str): ruta de la carpeta
        file_types (list) : lista de extensiones. Default = ['jpeg', 'jpg', 'png']
    Returns:
        list : lista de archivos
    """
    if not os.path.isdir(path):
        raise FileNotFoundError('Ruta no existente')
    dir_list = os.listdir(path)
    file_types = [f'.{e}' for e in file_types]
    dir_list = [e for e in dir_list if os.path.splitext(e)[1] in file_types]
    if len(dir_list) == 0:
        raise FileNotFoundError('No hay archivos con los tipos seleccionados')
    return dir_list