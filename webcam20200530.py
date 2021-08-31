import cv2 
import json
import face_recognition
import numpy as np
from numpy.lib.recfunctions import repack_fields
from photocut import photolo
from Facecode_List import functions
from function import cv2_word
from upload import uploads
from printrgb import layer


def outputvideo(self,frame,facelocation,member,time,commodstr,total,favorite): #影片輸出人臉資料之函數
    top, right, bottom, left = facelocation
    #/* 劃出框
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) 
    #*/
    frame = cv2.resize(frame,(1280,720),interpolation=cv2.INTER_CUBIC)
    h, w, c = frame.shape
    frame = graphics.output_graphics(frame,0.5,0,255,0,0,35,0,w/3.5)#畫正方圖形img,alphaReserve,BChannel,GChannel,RChannel,yMin,yMax,xMin,xMax
    frame = graphics.output_graphics(frame,0.4,150,150,150,35,65,0,w/3.5)
    frame = graphics.output_graphics(frame,0.5,0,255,0,65,100,0,w/3.5)
    frame = graphics.output_graphics(frame,0.4,150,150,150,100,280,0,w/3.5)
    frame = graphics.output_graphics(frame,0.5,0,0,255,280,315,0,w/3.5)
    frame = graphics.output_graphics(frame,0.4,150,150,150,315,h,0,w/3.5)
    font = cv2.FONT_HERSHEY_DUPLEX
    if (type(commodstr) == list):# old member
        frame = graphics.output_graphics(frame,0.4,198,198,198,bottom+20,bottom+90,left,right)
        cv2.putText(frame, member, (left, bottom + 50), font, 1.0, (0, 0, 0), 1)#顯示名字
        cv2.putText(frame,"NT : {}".format(total), (left, bottom + 80), font, 1.0, (0, 0, 0), 1) #顯示總金額
        cv2.putText(frame,"Time : ", (5,30), font, 1.0, (255, 255, 255), 1) #顯示上一次購物時間
        cv2.putText(frame,time, (5,55), font, 0.65, (255, 255, 255), 1) #顯示上一次購物時間
        cv2.putText(frame,"Purchase History :", (5,90), font, 1.0, (255, 255, 255), 1) #顯示購物紀錄
        ls = 95
        for i in range(len(commodstr)):
            s = i + 1
            ls += 30
            cv2.putText(frame,"{}.{}".format(s,commodstr[i]), (5, ls), font, 1.0, (255, 255, 255), 1) #顯示購物紀錄
       
        ls = 305
        cv2.putText(frame,"Maybe Favorite : ", (5,ls), font, 1.0, (255, 255, 255), 1) #顯示可能的喜好
        ls += 5
        for i in range(len(favorite)):
            if favorite[i] is "":
                break
            s = i + 1
            ls += 30
            cv2.putText(frame,"{}.{}".format(s,favorite[i]), (5, ls), font, 1.0, (255, 255, 255), 1) #顯示可能的喜好
    elif (type(commodstr) == str):# New member
        cv2.putText(frame,"New Member ID: ", (5,30), font, 1.0, (255, 255, 255), 1) #顯示ID
        cv2.putText(frame,member, (5,60), font, 0.6, (255, 255, 255), 1) 
        cv2.putText(frame,"Purchase History :", (5,90), font, 1.0, (255, 255, 255), 1) #顯示購物紀錄
        cv2.putText(frame,commodstr, (5, 125), font, 1.0, (255, 255, 255), 1)
    return frame


i = 0
video_capture = cv2.VideoCapture(0)
pil_img = photolo()
gets = functions()
output = cv2_word()
uploadfacecode = uploads()
graphics = layer()

image_to_test = face_recognition.load_image_file("obama.jpg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

while True:
    #/*讀取即時影像，如有人臉會輸出face_locations
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    #*/
    for face_location in face_locations: #face_locations有數值時執行
        photocuts = pil_img.cut(frame)
        facelocation = pil_img.locel(frame)
        if (photocuts is None):
            break
        image_encodings = face_recognition.face_encodings(photocuts)
        face_distances = face_recognition.face_distance(image_encodings, image_to_test_encoding) #  辨識即時人臉是否同一個人，如果是的話不會往下執行
   
        if (face_distances > 0.5): #有人臉的時候
            allfacedata = gets.Getface_Code()
            data = gets.Facecode_List() #取得資料庫人臉特徵碼
            image_encoding_numpys = np.asarray(image_encodings)
            for i in range(len(data)):
                datanumpy = np.asarray(data[i])
                face_konwdistances = face_recognition.face_distance(datanumpy,image_encoding_numpys) #開始對比人臉
                if (face_konwdistances < 0.5): #與資料庫有相符的人臉時候
                    member,commodstr,time,total,favorite = output.get_data(allfacedata[i])
                    break
                elif (i == len(data) - 1): #沒有相符的人臉時候
                    member,commodstr = uploadfacecode.upload_new_facecode(image_encoding_numpys)
                    print ("New Face")

            frame = outputvideo((),frame, facelocation, member, time, commodstr, total, favorite)
            image_to_test_encoding = image_encoding_numpys

        elif (face_distances < 0.5): #同一人的時候
            frame = outputvideo((),frame, facelocation, member, time, commodstr, total, favorite)

    frame = cv2.resize(frame,(1280,720),interpolation=cv2.INTER_CUBIC)
    cv2.imshow("camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



    
video_capture.release()
cv2.destroyAllWindows()
