from schemas.doctor import doctors

class DoctorService:
    @staticmethod
    def display_doctors(doctor_data):
        data = []
        for doctor in doctor_data:
            data.append(doctors[doctor])
        return data