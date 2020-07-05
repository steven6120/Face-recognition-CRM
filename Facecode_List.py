import urllib.request as requests
import json

class functions:
    def __init__(self):
        functions

    def Getface_Code(self):
        url = 'http://0.0.0.0:5000/facecode/all'
        response = requests.urlopen(url).read().decode('UTF-8')
        itemlist=json.loads(response)
        return itemlist

    def Facecode_List(self):
        url = 'http://0.0.0.0:5000/facecode/all'
        response = requests.urlopen(url).read().decode('UTF-8')
        data=json.loads(response)

        facecodes = []
        for facecode in data:
            facecodes.append(json.loads(facecode["Face_Code"]))
        return facecodes