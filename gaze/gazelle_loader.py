"""
    A very simple model manager that loads GazeLLE weights as static variables.
    Eliminates the need to load GazeLLE weights repeatedly.
"""

import torch

from gazelle.model import get_gazelle_model, GazeLLEv3
from settings import DEVICE

class GazeLLE:
    model_name = 'gazelle_v3_h'
    model: GazeLLEv3 = None
    transform = None

def load_gazelle():
    GazeLLE.model, GazeLLE.transform = get_gazelle_model(GazeLLE.model_name)
    GazeLLE.model.load_gazelle_state_dict(torch.load(f"./weights/{GazeLLE.model_name}.pt", weights_only=True))
    GazeLLE.model.to(DEVICE)
    GazeLLE.model.eval()

def get_gazelle():
    if GazeLLE.model is None or GazeLLE.transform is None:
        load_gazelle()
    return GazeLLE.model, GazeLLE.transform