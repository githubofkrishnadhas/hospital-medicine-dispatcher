import os
import pytz
import calendar
from datetime import datetime, timezone
class PatientDetails:
    patient_health_id = 0
    def __init__(self,name, age, day_of_birth,month_of_birth, year_of_birth, sex, is_new_patient=True):
        self.name = name
        self.age = age
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.sex = sex
        PatientDetails.patient_health_id += 1

        if is_new_patient:
            self.greet_patient()
            self.add_registration_date_time_to_patient_details()
            self.construct_date_of_birth_of_patient()
            self.add_registration_date_time_to_patient_details()
            self.get_month_name_from_month_integer()
            self.generate_registration_id()
        else:
            self.welcome_back_patient()


    def generate_registration_id(self):
        # Generate a registration ID based on the last assigned ID
        print(f"PID{PatientDetails.patient_health_id:05d}")
        return f"PID{PatientDetails.patient_health_id:05d}"


    def greet_patient(self):
        print(f"Welcome to devwithkrisha pharmacy registration system : {self.name}")


    def welcome_back_patient(self):
        print(f"Welcome back to devwithkrisha pharmacy : {self.name}")


    def add_registration_date_time_to_patient_details(self):
        ist_timezone = pytz.timezone('Asia/Kolkata')
        registration_date_time = datetime.now(ist_timezone)  # datetime(timezone= "Asia/Kolkata") # timezone("Asia/Kolkata"))
        print(registration_date_time)
        self.registration_date_time = registration_date_time



    def construct_date_of_birth_of_patient(self):
        date_of_birth = f"{self.day_of_birth}-{self.month_of_birth}-{self.year_of_birth}"
        print(f"Date of birth of {self.name} is {date_of_birth}")
        self.day_of_birth = date_of_birth


    def get_month_name_from_month_integer(self):
        month_interger_value = self.month_of_birth
        monthname = calendar.month_name[month_interger_value]
        print(f"Month name of integer {self.month_of_birth} is : {monthname}")




def access_class():
    """

    :return:
    """
    # class_p = PatientDetails()
    user1 = PatientDetails("Krish", 22, 13, 12, 1997, "Male", 112)
    print(user1)

    print(user1.patient_health_id)

access_class()