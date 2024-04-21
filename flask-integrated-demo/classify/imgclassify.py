###################################################################################################
### Reference:
### https://learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models/
###################################################################################################

from torchvision import models
from torchvision import transforms
import torch
from PIL import Image
from classify.imgtolabel import img_to_label

def img_classify(path):

    #transform to reshape input for model
    transform = transforms.Compose([            
        transforms.Resize(256),                    
        transforms.CenterCrop(224),                
        transforms.ToTensor(),                 
        transforms.Normalize(                      
            mean=[0.485, 0.456, 0.406],                
            std=[0.229, 0.224, 0.225]                  
        )])

    #load input image and apply transform
    img = Image.open(path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    #load image classification model and run
    resnet = models.resnet50(pretrained=True)
    resnet.eval()
    out = resnet(batch_t)
    _, indices = torch.sort(out, descending=True)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    return img_to_label[indices[0][0].item()]
    