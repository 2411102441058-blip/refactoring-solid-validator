class ValidatorManager:
    def validate(self, student):
        print("Memulai validasi (SEBELUM refactoring)...")

        if student["sks"] < 20:
            print("❌ Validasi SKS gagal")
            return False

        if not student["prasyarat"]:
            print("❌ Validasi Prasyarat gagal")
            return False

        print("✅ Semua validasi lolos")
        return True


student = {"sks": 18, "prasyarat": True}
manager = ValidatorManager()

print("HASIL AKHIR:", manager.validate(student))
