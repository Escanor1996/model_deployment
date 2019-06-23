import io

import torch 
import torch.nn as nn
from torchvision import models,transforms
from PIL import Image 


def get_model():
	checkpoint_path='classifier.pt'
	model=models.densenet121(pretrained=True)
	model.classifier=nn.Linear(1024,102)
	model.load_state_dict(torch.load(checkpoint_path,map_location='cpu'),strict=False)
	model.eval()
	return model

def get_tensor(image_bytes):
	my_transforms=transforms.Compose([transforms.Resize(255),
		                              transforms.CenterCrop(224),
		                              transforms.ToTensor(),
		                              transforms.Normalize(
		                              	[0.485,0.456,0.406],
		                              	[0.229,0.224,0.225])])
	image=Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)