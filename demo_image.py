from PIL import Image
import torch
import torch.nn.functional as F
from gazelle.model import get_gazelle_model
import os
import numpy as np

model_name = 'gazelle_v3_h'
model, transform = get_gazelle_model(model_name)
model.load_gazelle_state_dict(torch.load(f"./weights/{model_name}.pt", weights_only=True))
model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# image name and facial bounding box
images = [
    (
        '1.png',
        [190, 93, 251, 169]
    ),
    (
        '2.png',
        [159, 91, 235, 189]
    ),
]


for filename, bbox in images:
    image = Image.open(os.path.join('demo_images', filename)).convert("RGB")
    width, height = image.size

    bbox = np.array(bbox) / np.array([width, height, width, height])

    input = {
        "images": transform(image).unsqueeze(dim=0).to(device),    # tensor of shape [1, 3, 448, 448]
        "bboxes": [[bbox]]              # list of lists of bbox tuples
    }

    with torch.no_grad():
        output = model(input)
    predicted_heatmap = output["heatmap"][0][0]        # access prediction for first person in first image. Tensor of size [64, 64]
    # predicted_inout = output["inout"][0][0]            # in/out of frame score (1 = in frame) (output["inout"] will be None  for non-inout models)


    import matplotlib.pyplot as plt
    from gazelle.utils import visualize_heatmap

    viz = visualize_heatmap(image, predicted_heatmap, bbox)
    plt.imshow(viz)
    plt.show()