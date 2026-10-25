from abc import ABC, abstractmethod
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from transformers import AutoModel, AutoImageProcessor
import os

# Abstract Backbone class
class Backbone(nn.Module, ABC):
    def __init__(self):
        super(Backbone, self).__init__()
    
    @abstractmethod
    def forward(self, x):
        pass

    @abstractmethod
    def get_dimension(self):
        pass

    @abstractmethod
    def get_out_size(self, in_size):
        pass

    def get_transform(self):
        pass


# DINOv3 backbone implemented with huggingface transformers
class DinoV3Backbone(Backbone):
    def __init__(self, model_name, from_local_file=False):
        super(DinoV3Backbone, self).__init__()
        if from_local_file:
            self.model = AutoModel.from_pretrained(
                f'dinov3/{model_name}',
                local_files_only=True
            )
        else:
            self.model = AutoModel.from_pretrained(f"facebook/{model_name}-pretrain-lvd1689m")
        self.patch_size = 16  # dinov3 has fixed 16*16 patches
        if model_name == 'dinov3_vitb16':
            self.embed_dim = 768  
        elif model_name == 'dinov3_vitl16':
            self.embed_dim = 1024  
        elif model_name == 'dinov3_vith16plus':
            self.embed_dim = 1280  

    def forward(self, x):
        b, c, h, w = x.shape
        out_h, out_w = self.get_out_size((h, w))
        with torch.inference_mode():
            x = self.model(x)
        x = x.last_hidden_state  # B, 1 CLS + 4 REG + N patch tokens, embed_dim
        register_tokens = x[:, 1: 5, :]  # B, 4, embed_dim
        patch_tokens = x[:, 5:, :]  # B, out_h * out_w, embed_dim
        x = patch_tokens.view(b, out_h, out_w, -1).permute(0, 3, 1, 2)  # b, embed_dim, out_h, out_w
        return x, register_tokens
    
    def get_dimension(self):
        return self.embed_dim
    
    def get_out_size(self, in_size):
        h, w = in_size
        return (h // self.patch_size, w // self.patch_size)
    
    def get_transform(self, in_size):
        return transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize(in_size),
            transforms.Normalize(
                mean=[0.485,0.456,0.406],
                std=[0.229,0.224,0.225]
            ),
        ])