class ForwardChainingPlantExpert:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def get_user_input(self, symptom):
        while True:
            user_input = input(f"Apakah tanaman padi mengalami gejala {symptom}? (Yes/No): ").lower()
            if user_input in ["yes", "no"]:
                return user_input
            else:
                print("Masukkan tidak valid. Harap masukkan 'Yes' atau 'No'.")

    def diagnose(self):
        print("Proses Forward Chaining untuk Diagnosa Hama dan Penyakit Tanaman Padi")

        user_input_yellowing = self.get_user_input("Daun Menguning")
        if user_input_yellowing == "yes":
            print("Gejala: Daun Menguning")
            
            user_input_spotting = self.get_user_input("Bercak pada Daun")
            if user_input_spotting == "yes":
                print("Gejala: Bercak pada Daun")
                print("Aturan: Terdapat kemungkinan serangan penyakit Y.")
                print("Diagnosis: Tanaman padi mengalami serangan penyakit Y.")
                
            else:
                user_input_dark_stem = self.get_user_input("Gelap pada Batang")
                if user_input_dark_stem == "yes":
                    print("Gejala: Gelap pada Batang")
                    print("Aturan: Terdapat kemungkinan serangan hama Z.")
                    print("Diagnosis: Tanaman padi diserang oleh hama Z.")
                    
                else:
                    print("Diagnosis: Perlu dilakukan analisis lebih lanjut.")
                    
        else:
            print("Diagnosis: Tanaman padi tidak menunjukkan gejala yang signifikan.")


if __name__ == "__main__":
    plant_expert = ForwardChainingPlantExpert()
    plant_expert.add_fact("Daun Menguning")
    plant_expert.add_fact("Bercak pada Daun")
    plant_expert.diagnose()
