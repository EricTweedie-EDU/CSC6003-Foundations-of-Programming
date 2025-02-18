# Program that maintains hospital records for personnel: Doctors, Surgeons, and Nurses
# the main parent class is the Personnel class

class Personnel:
    '''Parent class for all personnel in the hospital'''
    def __init__(self, name, age, hourlyRate):
        self.name = name
        self.age = age
        self.hourlyRate = hourlyRate

    def display():
        print(f"My name is {self.name} and I am {self.age} years old.")

class Doctor(Personnel):
    '''Child class for doctors'''
    def __init__(self, name, age, hourlyRate, specialty):
        super().__init__(name, age, hourlyRate)
        self.specialty = specialty

    def displayDoctor(self):
        print(f"My name is {self.name} and I am {self.age} years old. I am a {self.specialty} doctor.")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_hourlyRate(self):
        return self.hourlyRate

    def get_specialty(self):
        return self.specialty

class Surgeon(Personnel):
    '''Child class for surgeons'''
    def __init__(self, name, age, hourlyRate, boardCertified):
        super().__init__(name, age, hourlyRate)
        self.boardCertified = boardCertified

    def displaySurgeon(self):
        print(f"My name is {self.name} and I am {self.age} years old. I am a {self.boardCertified} surgeon.")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_hourlyRate(self):
        return self.hourlyRate

    def get_boardCertified(self):
        return self.boardCertified

class Nurse(Personnel):
    '''Child class for nurses'''
    def __init__(self, name, age, hourlyRate, rank):
        super().__init__(name, age, hourlyRate)
        self.rank = rank

    def displayNurse(self):
        print(f"My name is {self.name} and I am {self.age} years old. I am a {self.rank} rank nurse.")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_hourlyRate(self):
        return self.hourlyRate

    def get_rank(self):
        return self.rank

doctor = Doctor("John", 34, 50, "Cardiology")
doctor.displayDoctor()
surgeon = Surgeon("Mary", 42, 60, "Board Certified")
surgeon.displaySurgeon()
nurse = Nurse("Jane", 28, 40, "Senior")
nurse.displayNurse()