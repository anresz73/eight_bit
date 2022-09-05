import os
import numpy as np
from pyxelate import Pyx, Pal
from skimage import io, img_as_ubyte
from skimage.color import rgb2gray
from skimage.transform import resize

# Efectos
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

def custom_grey(array_image):
    """
    Devuelve array convertido a escala de grises
    Args:
        array_image (numpy array): array con la imagen descargada
    Returns:
        numpy array: array con imagen en escala de grises
    """
    if len(array_image.shape) == 3:
        array_result = np.dot(array_image[..., :3], [.299, .587, .114])
    else:
        print('Ya está en grises')
        array_result = array_image[:]
    # Uint8 Converter
    imin, imax = array_result.min(), array_result.max()
    a = (255 - 0) / (imax - imin) # Fórmula 255 a 0
    b = 255 - a * imax
    array_result = (a * array_result + b).astype(np.uint8)
    return array_result

def image_resize(array_image, size = (569, 857)):
    """
    Devuelve array de la imagen reducido por el factor dado
    Args:
        array_image (np array): array de la imagen
        factor (int): Factor a reducir. Defaults = 10.

    Returns:
        numoy array: array con la imgen resizeada
    """
    #new_shape = (
    #    array_image.shape[0] // factor,
    #    array_image.shape[1] // factor,
    #    array_image.shape[2])
    new_shape = size + (3,)
    resized_array = resize(
        image = array_image,
        output_shape = new_shape)
    return img_as_ubyte(resized_array)

# Archivos
def read_image(image_path):
    """
    Lee y devuelve array a partir de ruta de imagen
    Args:
        image_path (str): ruta del archivo imagen
    Returns:
        numpy array: array con la imagen
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f'Archivo {image_path} no existe')
    result_array = io.imread(image_path)
    return result_array

def save_image(image_path, image_array, extra_str = 'new'):
    """
    Guarda la imagen a partir de array
    Args:
        image_path (str): ruta para guardar la imagen
        image_array (np array): array con la imagen
        extra_str (str) : extra str para el nombre
    """
    split_path = os.path.split(image_path)
    if not isinstance(image_array, np.ndarray):
        raise TypeError(f'Imagen {split_path[1]} no es un numpy array')
    io.imsave('{}/{}_{}'.format(split_path[0], extra_str, split_path[1]), image_array)

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
        raise FileNotFoundError(f'Ruta {path} no existente')
    dir_list = os.listdir(path)
    file_types = [f'.{e}' for e in file_types]
    dir_list = [e for e in dir_list if os.path.splitext(e)[1] in file_types]
    if len(dir_list) == 0:
        raise FileNotFoundError('No hay archivos con los tipos seleccionados')
    return dir_list

