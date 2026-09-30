import random


def register_patient(name, age, disease):
    token = random.randint(1000, 9999)
    return {"name": name, "age": age, "disease": disease, "token": token}
