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


directory_hyou = './proposed_image/'
directory_result ='./proposed_result/'

for num in range(40):
    img_hyou = Image.open(directory_hyou + "proposed_" + str(num).zfill(2) + ".png")
    img_result = Image.open(directory_result + str(num).zfill(2) + ".png")
    img = Image.new("RGB", (1200, 800), (255, 255, 255))
    img.paste(img_hyou, (0, 0), img_hyou.split()[3])
    img.paste(img_result, (800, 200))
    img.save("./test/{}".format(str(num).zfill(2) + ".png"))


"""
758,777
384,256
"""
