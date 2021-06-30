import os
import numpy as np
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils import data
from torchvision import transforms, utils
from tqdm import tqdm
torch.backends.cudnn.benchmark = True
import copy
from io import BytesIO
from impachu.models.gans_n_roses.util import *
from PIL import Image

from impachu.models.gans_n_roses.model import *
import moviepy.video.io.ImageSequenceClip
import scipy
import cv2
import dlib
import requests
import kornia.augmentation as K
from IPython.display import Video


class GANsNRoses:

    def __init__(self):
        self.composition = None
        self.image_url = ''
        return

    def get_result(self):
        """
        Returns the edited image as a BytesIO object
        """
        arr = BytesIO()
        self.composition.save(arr, format="PNG")
        arr.seek(0)
        return arr

    def run_inference(self, url, seed=0):
        latent_dim = 8
        n_mlp = 5
        num_down = 3

        G_A2B = Generator(256, 4, latent_dim, n_mlp, channel_multiplier=1, lr_mlp=.01,n_res=1).eval()

        ensure_checkpoint_exists('GNR_checkpoint.pt')
        ckpt = torch.load('GNR_checkpoint.pt', map_location=lambda storage, loc: storage)

        G_A2B.load_state_dict(ckpt['G_A2B_ema'])

        # mean latent
        truncation = 1
        with torch.no_grad():
            mean_style = G_A2B.mapping(torch.randn([1000, latent_dim])).mean(0, keepdim=True)

        test_transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5), inplace=True)
        ])

        plt.rcParams['figure.dpi'] = 200

        if seed:
            torch.manual_seed(seed)

        num_styles = 5
        style = torch.randn([num_styles, latent_dim])

        response = requests.get(url)
        real_A = Image.open(BytesIO(response.content))
        real_A = test_transform(real_A).unsqueeze(0)

        with torch.no_grad():
            A2B_content, _ = G_A2B.encode(real_A)
            fake_A2B = G_A2B.decode(A2B_content.repeat(num_styles,1,1,1), style)
            A2B = torch.cat([real_A, fake_A2B], 0)

        self.composition = transforms.ToPILImage()(utils.make_grid(A2B.cpu(), normalize=True, range=(-1, 1), nrow=10))
