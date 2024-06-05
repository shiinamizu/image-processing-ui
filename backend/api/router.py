from fastapi import APIRouter, Response
from fastapi.responses import StreamingResponse
import sys
import cv2
import io
import base64

from services.segmentation import calculate
from services.changecolor import translate
from services.getImage import getImage 
from services.extructColors import extruct

router = APIRouter()


@router.get("/api/image")
def readImage():

    with open("./media/test2.jpg", "rb") as img:
        base64_data = base64.b64encode(img.read()).decode('utf-8')

        return {"image" : base64_data}

@router.get("/api/segmentation")
def segmentationImage():
    # print("test")
    output = calculate()
    return {"responce": "segmentation"}

@router.get("/api/changecolor")
def changecolor():
    print("testf")
    output = translate()
    return {"responce": "translate"}

@router.get("/api/extruct")   
def extructColor():
    # print("test")
    output = extruct()
    return {"responce": "extruct"}


