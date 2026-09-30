doctors = [
    {"name": "Dr. Subhashree Sanu", "speciality": "Heart", "fee": 1500},
    {"name": "Dr. Hannibal", "speciality": "Skin", "fee": 800},
]


def assign_doctor(speciality):
    for d in doctors:
        if d["speciality"] == speciality:
            return d
    return doctors[0]
