import json
import os

def save_lead(data: dict):
    file = "leads.json"
    if os.path.exists(file):
        with open(file, "r") as f:
         contenido = json.load(f)
    else:
        contenido = []
    contenido.append(data)
    with open(file, "w") as f:
        json.dump(contenido, f, indent=4)


def read_leads():
    file = "leads.json"
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []