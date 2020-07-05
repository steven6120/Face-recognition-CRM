import face_recognition

class photolo:

        def __init__(self):
            photolo
    
        def cut(self,image):
            face_locations = face_recognition.face_locations(image)
            #*/重新排序face_locations，最靠近鏡頭的人放在face_locations[0]
            def takeSecond(elem):
                return elem[0]
            face_locations.sort(key=takeSecond)
            #/*
            for face_location in face_locations:
                top, right, bottom, left = face_location
                face_image = image[top:bottom, left:right]
                return face_image
                
        def locel(self,image):
            face_locations = face_recognition.face_locations(image)
            #*/重新排序face_locations，最靠近鏡頭的人放在face_locations[0]
            def takeSecond(elem):
                return elem[0]
            face_locations.sort(key=takeSecond)
            #/*
            for face_location in face_locations:
                top, right, bottom, left = face_location
                return face_location





    
