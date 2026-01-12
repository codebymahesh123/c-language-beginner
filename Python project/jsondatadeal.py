import json

def data_file(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        return data

data=data_file("amz.json")
print(data)
