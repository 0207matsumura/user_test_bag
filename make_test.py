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


directory = './FUNIT/'
image_list = os.listdir(directory)


for image in image_list:
    url = directory + image
    img = Image.open(url)
    #print(img.width)
    #print(img.height)
    img = img.resize((int(1.5*img.width), int(1.5 *img.height)) )
    img.save("FUNIT_test/{}".format(image))
