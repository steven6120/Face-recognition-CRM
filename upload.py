import requests

class uploads:
    def __init__(self):
        uploads
        
    def upload_new_facecode(self, image_encodings):
        url = 'http://0.0.0.0:5000/facecode/all'
        ##image_encodings list(can`t change json) to new list(can change json) 

        list_image_encondings = []


        for i in range(len(image_encodings)):
            dict1 = {}
            list1 = []
            for j in range(len(image_encodings[i])):
                list1.append(image_encodings[i][j])
            dict1['Face_Code'] = list1
            dict1['UserID'] = "none"
            list_image_encondings.append(dict1)

        ##------------       
        headers = {
            'Content-Type': 'application/json',
            'Content-Type': 'text/plain'
        }
        r = requests.request("POST", url, headers = headers,json = list_image_encondings[0])

        itemlist = eval(r.text) #轉成list

        member = itemlist["UserID"]
        commodstr = "New member"
           
        return member,commodstr

