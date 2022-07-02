import os
import requests

dir = os.path.join(os.path.expanduser("~"), "supplier-data", "descriptions")
files = os.listdir(dir)


def serialize(files):
    for file in files:
        data = {}
        with open(dir + "/" + file) as txt:
            lines = txt.readlines()
            data["name"] = lines[0].strip()
            weight = lines[1].strip().split()
            data["weight"] = int(weight[0])
            data["description"] = lines[2].strip()
            image = os.path.splitext(file)[0]
            data["image_name"] = image + ".jpeg"
        web_upload(data)



def web_upload(data):
    p = data
    r = requests.post("http://<ip>/fruits/", json=p)
    r.raise_for_status()



serialize(files)