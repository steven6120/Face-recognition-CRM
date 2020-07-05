import cv2

class layer:
    def __init__(self):
        layer

    def output_graphics(self,img,alphaReserve,BChannel,GChannel,RChannel,yMin,yMax,xMin,xMax):
        img[yMin:yMax, xMin:int(xMax), 0] = img[yMin:yMax, xMin:int(xMax), 0] * alphaReserve + BChannel * (1 - alphaReserve)
        img[yMin:yMax, xMin:int(xMax), 1] = img[yMin:yMax, xMin:int(xMax), 1] * alphaReserve + GChannel * (1 - alphaReserve)
        img[yMin:yMax, xMin:int(xMax), 2] = img[yMin:yMax, xMin:int(xMax), 2] * alphaReserve + RChannel * (1 - alphaReserve)
        return img

