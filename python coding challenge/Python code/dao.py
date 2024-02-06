# Package: dao

from abc import ABC, abstractmethod
from typing import List
from entity import Appointment
from exception import AppointmentNotFoundException, DoctorNotFoundException, PatientNumberNotFoundException
from util import DBConnection, DBConnectionException 


conn = DBConnection.get_connection()
cursor = conn.cursor()

class IHospitalService(ABC):
    @abstractmethod
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        try:
            query = "SELECT * FROM Appointment WHERE appointmentID = %s"
            cursor.execute(query, (appointment_id,))  # Use parameterized query for safety

            result = cursor.fetchone()  # Fetch a single row

            if result:
                # Create Appointment object from the fetched data
                appointment = Appointment(*result)  # Assuming Appointment class has a matching constructor
                print("Appointment data with appointmentID", appointment_id, "fetched successfully")
                return appointment
            else:
                print("Appointment data with appointmentID", appointment_id, "not found")
                return None

        except DBConnectionException as e:
            print("Failed to fetch appointment:", e)
            return None
        finally:
            cursor.close()  

    @abstractmethod
    def get_appointments_by_patient_id(self, patient_id: int) -> List[Appointment]:
        try:
            query = "SELECT * FROM Appointment WHERE patientID = %s"
            cursor.execute(query, (patient_id,))  # Parameterized query for safety

            appointments = []
            results = cursor.fetchall()  # Fetch all matching appointments
            for row in results:
                appointment = Appointment(*row)  # Create Appointment object
                appointments.append(appointment)

            if appointments:
                print("Appointment data with patientID", patient_id, "fetched successfully")
                return appointments
            else:
                raise PatientNumberNotFoundException(patient_id)

        except DBConnectionException as e:
            print("Failed to fetch appointments:", e)
            raise  # Re-raise to handle at a higher level
        finally:
            cursor.close() 

    @abstractmethod
    def get_appointments_for_doctor(self, doctor_id: int) -> List[Appointment]:
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """
                SELECT *
                FROM Appointment
                WHERE doctorId = %s
            """
            cursor.execute(query, (doctor_id,))
            results = cursor.fetchall()

            if results:
                appointments = []
                for row in results:
                    appointment = Appointment(*row)  # Assuming Appointment class exists
                    appointments.append(appointment)

                return appointments
            else:
                raise DoctorNotFoundException(f"Doctor with ID {doctor_id} not found")

        except DBConnectionException as e:
            raise  
        finally:
            if cursor:
                cursor.close()
    

    @abstractmethod
    def cancel_appointment(self, appointment_id: int) -> bool:
        try:
            query = "DELETE FROM Appointment WHERE appointmentID = %s"
            cursor.execute(query, (appointment_id,)) 

            conn.commit()  # Commit the deletion
            print("Appointment with ID", appointment_id, "deleted successfully")

        except DBConnectionException as e:
            raise  
        finally:
            if cursor:
                cursor.close()
    
    @abstractmethod
    def schedule_appointment(self, appointment: Appointment) -> bool:
        """Schedules a new appointment."""
        pass

    @abstractmethod
    def update_appointment(self, appointment: Appointment) -> bool:
        """Updates an existing appointment."""
        pass

class HospitalServiceImpl(IHospitalService):

    def __init__(self, db_util):
        self.db_util = db_util

    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        # Fetch appointment data from database using appointment_id and db_util
        # Raise AppointmentNotFoundException if not found
        appointment_data = self.db_util.fetch_appointment_by_id(appointment_id)
        if not appointment_data:
            raise AppointmentNotFoundException(f"Appointment with ID {appointment_id} not found")
        return Appointment(**appointment_data) 

    def get_appointments_for_patient(self, patient_id: int) -> List[Appointment]:
        # Retrieve appointments for the given patient_id using db_util
        appointment_data_list = self.db_util.fetch_appointments_for_patient(patient_id)
        return [Appointment(**data) for data in appointment_data_list]

    def get_appointments_for_doctor(self, doctor_id: int) -> List[Appointment]:
        # ... (Similar implementation using db_util)
        pass

    def schedule_appointment(self, appointment: Appointment) -> bool:
        # Add appointment to database using db_util
        return self.db_util.add_appointment(appointment)

    def update_appointment(self, appointment: Appointment) -> bool:
        # Update appointment in database using db_util
        return self.db_util.update_appointment(appointment)

    def cancel_appointment(self, appointment_id: int) -> bool:
        # Cancel appointment in database using db_util
        return self.db_util.cancel_appointment(appointment_id)
