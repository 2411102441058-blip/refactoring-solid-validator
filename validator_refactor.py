from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def validate(self, student):
        pass


class SKSValidator(Validator):
    def validate(self, student):
        print("Cek SKS mahasiswa...")
        return student["sks"] >= 20


class PrasyaratValidator(Validator):
    def validate(self, student):
        print("Cek prasyarat mata kuliah...")
        return student["prasyarat"]


class ValidatorManager:
    def __init__(self, validators):
        self.validators = validators

    def validate(self, student):
        print("Memulai validasi (SESUDAH refactoring)...")
        for validator in self.validators:
            if not validator.validate(student):
                print("❌ Validasi gagal")
                return False
        print("✅ Semua validasi lolos")
        return True


student = {"sks": 22, "prasyarat": True}
validators = [SKSValidator(), PrasyaratValidator()]
manager = ValidatorManager(validators)

print("HASIL AKHIR:", manager.validate(student))
