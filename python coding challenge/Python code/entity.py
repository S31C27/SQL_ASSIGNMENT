# Package: entity

# Patient class
class Patient:
    def _init_(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self.patientId = patientId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address

    def _str_(self):
        return f"Patient ID: {self.patientId}, Name: {self.firstName} {self.lastName}, DOB: {self.dateOfBirth}, Gender: {self.gender}, Contact: {self.contactNumber}, Address: {self.address}"

# Doctor class
class Doctor:
    def _init_(self, doctorId, firstName, lastName, specialization, contactNumber):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

    def _str_(self):
        return f"Doctor ID: {self.doctorId}, Name: {self.firstName} {self.lastName}, Specialization: {self.specialization}, Contact: {self.contactNumber}"

# Appointment class
class Appointment:
    def _init_(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def _str_(self):
        return f"Appointment ID: {self.appointmentId}, Patient ID: {self.patientId}, Doctor ID: {self.doctorId}, Date: {self.appointmentDate}, Description: {self.description}"
