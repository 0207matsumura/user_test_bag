import os, os.path
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader
from torch import optim
from torch import nn
from tqdm import tqdm
import numpy as np
import torch
from torchvision import models
from PIL import Image


directory_hyou = './compared_image/'
directory_result = './FUNIT_result_2/'

for num in range(40):
    img_hyou = Image.open(directory_hyou + "compared_" + str(num).zfill(2) + ".png")
    img_result = Image.open(directory_result + str(num).zfill(2) + ".png")
    img = Image.new("RGB", (1200, 800), (255, 255, 255))
    
    img_hyou = img_hyou.resize((int(0.9 * img_hyou.width), int(0.9 * img_hyou.height)))
    img.paste(img_hyou, (0, 0), img_hyou.split()[3])
    img_result = img_result.resize((500, 750))
    img.paste(img_result, (700, 0))
    img.save("./FUNIT_user/{}".format(str(num).zfill(2) + ".png"))


"""
758,777
384,256
442
"""

