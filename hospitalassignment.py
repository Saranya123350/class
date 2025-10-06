class hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctors(self, doctors_list):
        self.doctors.extend(doctors_list)   
        print("doctors added to the hospital")

    def addPatients(self, patients_list):
        self.patients.extend(patients_list)
        print("patients added to the hospital")

    def addAppointments(self, appointments_list):
        self.appointments.extend(appointments_list)
        print("appointments added to the hospital")


class doctors:
    def __init__(self, doctor_id, doctor_name, specialist, phone_no, avaliablity="daily"):
        self.id = doctor_id
        self.doctor_name = doctor_name     
        self.specialist = specialist
        self.avaliability = avaliablity
        self.phone_no = phone_no
        self.patients = []                 
        self.appointments = []            
        self.history = []

    def view_appointments(self):
        print(f"Appointments for Doctor {self.doctor_name} : ")
        for apt in self.appointments:
            print(f"Appointment for appointment id {apt.appointment_id} patient {apt.patient.patient_name} is on {apt.date} at {apt.time} --> {apt.status}")

    def addpatientreport(self, appointment, notes):
        if appointment in self.appointments:
            appointment.review = notes
            appointment.status = "completed"
            self.history.append((appointment.patient.patient_name, notes))
            print(f"Notes added for {appointment.patient.patient_name}")

    def checkPatient(self):
        for record in self.history:
            print(f"{self.doctor_name} diagnosed {record[0]} with {patients.self.medical_history} and final report notes on patient is : {record[1]}")


class patients:
    def __init__(self, patient_id, patient_name, age, gender, medical_history, current_problem=None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.gender = gender
        self.current_problem = current_problem
        self.medical_history = medical_history
    def viewHistory(self):
        print(f"{self.patient_name}'s medical history: {self.medical_history}")


class appointments:
    def __init__(self, appointment_id, date, time, doctor=None, patient=None, status="scheduled"):
        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.patient = patient       
        self.doctor = doctor         
        self.status = status
        self.review = None


H = hospital()

D1 = doctors(101, "sai", "cardiologist", 123456789, "Weekdays")
D2 = doctors(102, "Micheal", "Neurologist", 2346529876, "Daily")
D3 = doctors(103, "shila", "Orthologist", 7403956856, "wednesday")

P1 = patients(1000, "raju", 18, "Male", "None", "Fever,cold")
P2 = patients(1001, "sarada", 62, "Female", "Diabetes,Bp", "Cough,fever")

A1 = appointments(300, "3-oct-2035", "7:00", D1, P1, "completed")
A2 = appointments(301, "6-Nov-2025", "11:15", D2, P2, "scheduled")
A3 = appointments(302, "30-Nov-2025", "12:00", D3, P1, "cancelled")

Doctor_list = [D1, D2, D3]
Patient_list = [P1, P2]
Appointment_list = [A1, A2, A3]

H.addDoctors(Doctor_list)
H.addAppointments(Appointment_list)
H.addPatients(Patient_list)

D1.appointments.append(A1)
D2.appointments.append(A2)
D3.appointments.append(A3)

D1.view_appointments()
D1.addpatientreport(A1, "Patient recovered")
D1.checkPatient()
P2.viewHistory()
