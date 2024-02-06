from dao import HospitalService
from exception import PatientNumberNotFoundException

class HospitalApp:
    def __init__(self):
        self.hospital_service = HospitalService()

    def run(self):
        while True:
            print("Select options:")
            print("1. Get appointment by appointment ID")
            print("2. Get appointment by patient ID")
            print("3. Cancel/Delete appointment by appointment ID")
            print("4. Get all appointments of doctor by doctor ID")
            print("******************")
            option = int(input("Enter number to perform operations: "))

            if option == 0:
                break

            try:
                if option == 1:
                    appointment_id = int(input("Enter appointment ID: "))
                    self.hospital_service.get_appointmentById(appointment_id)
                elif option == 2:
                    patient_id = int(input("Enter patient ID: "))
                    self.hospital_service.get_appointmentBypatientId(patient_id)
                elif option == 3:
                    appointment_id = int(input("Enter appointment ID to cancel: "))
                    self.hospital_service.cancelAppointment(appointment_id)
                elif option == 4:
                    doc_id = int(input("Enter doctor ID to fetch all appointments: "))
                    self.hospital_service.get_all_appointmentByDoctorId(doc_id)
                else:
                    print("Invalid option")
            except PatientNumberNotFoundException as e:
                print(e)
            except Exception as e:
                print("An error occurred:", e)  # Handle other potential errors

if __name__ == "__main__":
    app = HospitalApp()
    app.run()
