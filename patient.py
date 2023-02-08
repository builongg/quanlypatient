class Patient:

    count = 0

    def __init__(self , id , name):
        self.id = id
        self.name = name
        Patient.count += 1

    # def set_id(self , id):
    #     self.id = id

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def show_info(self):
        print(f"\nThông tin bệnh nhân :  \n")
        print(f"Id :  { self.get_id() }")
        print(f"Tên bệnh nhân :  { self.name }")