class PatientNumberNotFoundException(Exception):
    """Raised when a patient with the given number is not found in the database."""

    def __init__(self, patient_number):
        super().__init__(f"Patient with number {patient_number} not found.")
        self.patient_number = patient_number


class AppointmentNotFoundException(Exception):
    pass

class DoctorNotFoundException(Exception):
    """Exception raised when a doctor with the given ID is not found."""
