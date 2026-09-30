import importlib
import sys

import appointment as ap
import billing
import doctor
import patient
from billing import generate_bill

if __name__ == "__main__":
    print("------ HOSPITAL MANAGEMENT SYSTEM ------")
    p = patient.register_patient("Jophin",22, "Heart")
    print("Patient Registered Successfully")
    print("Patient Name:", p["name"])
    d = doctor.assign_doctor("Heart")
    print("Doctor Assigned:", d["name"])
    a = ap.schedule_appointment(p, d)
    print("Appointment Date:")
    print(a["date"])
    print("Generated Token Number:")
    print(p["token"])
    print("Bill Amount:")
    print(generate_bill(d["fee"], 1000))
    print("Current Module Name:")
    print(__name__)
    print("Imported Modules:")
    print(patient.__name__)
    print(doctor.__name__)
    print(billing.__name__)
    print("Python Search Paths:")
    print(sys.path)
    importlib.reload(patient)
    print("Module Reloaded Successfully")
    print("Thank You for Using Hospital Management System")
