import json


def saveFileByJson(Json,fileName):
    with open(fileName, 'w', encoding='utf-8') as json_file:
        json.dump(Json, json_file, ensure_ascii=False)
        print("write json file success!")

def loadJsonFromFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data