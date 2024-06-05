import segmentation_models_pytorch as smp
import cv2
import torch
import numpy as np

from services.generate_segimage import generate

def calculate():
    class_num =6
    model = smp.Unet(
        encoder_name="efficientnet-b7",        # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
        encoder_weights="imagenet",     # use `imagenet` pre-trained weights for encoder initialization
        in_channels=3,                  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
        classes=class_num,                      # model output channels (number of classes in your dataset)
    )

    inputIm = cv2.imread("./media/test5.jpg")
    inputIm = cv2.resize(inputIm,(512,256))
    inputs =torch.from_numpy(inputIm.astype(np.float32)).clone()
    inputs = torch.permute(inputs,(2,0,1))
    inputs = torch.reshape(inputs,(1,3,256,512))


    output = model(inputs)
    # print(output)
    output = torch.reshape(output,(class_num,256,512))
    # output = torch.permute(output,(1,2,0))
    
    outputIm = output.to('cpu').detach().numpy().copy()
    out = generate(outputIm,0.8)
    # outputIm = outputIm *255
    cv2.imwrite("./media/output.jpg",out)

    return out
