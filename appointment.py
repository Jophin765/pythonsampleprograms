import datetime


def schedule_appointment(patient, doctor):
    return {
        "patient": patient["name"],
        "doctor": doctor["name"],
        "date": datetime.date.today()  # noqa: DTZ011
    }
