import numpy as np
import cv2
import requests
import json
import function

class cv2_word:
    def __init__(self):
        cv2_word
        
    def get_data(self, stre):
        url = 'http://0.0.0.0:5000/facecode/all'
        headers = {
            'Content-Type': 'application/json',
            'Content-Type': 'text/plain'
        } #資料處理
        r = requests.post(url, headers = headers,json = stre) #post資料
        itemlist = eval(r.text) #轉成list
        if (type(itemlist) == list):
            i = 0
            commod = []
            favorite = []
            for item in itemlist:
                if i == 0: #判斷是不是第一筆資料
                    member = item["MemberName"]
                    i = i+1
                elif i == 1:
                    for s in range(3):
                        e = s + 1
                        favorite.append(item["Favorite0{}".format(e)])
                    i = i+1
                else:
                    commod.append(item["Commodity"])
                    time = item["PurchaseTime"]
                    total = item["TotalAmount"]


        elif (type(itemlist) == str):
            time,total,favorite = ("","","")
            member = stre["UserID"]
            commod = itemlist
            
        return member,commod,time,total,favorite


       