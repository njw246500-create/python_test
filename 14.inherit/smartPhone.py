class Phone : 
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self, target_number) : 
        print(f'{target_number}번호로 전화를 겁니다')

class Camera : 
    def __init__(self,megapixels):
        self.megapixels = megapixels

    def take_photo(self) : 
        print(f"{self.megapixels}만 화소로 촬영합니다.")

class SmartPhone(Phone, Camera) : 
    def __init__(self,phone_number,megapixels,model_name) :
        Phone.__init__(self, phone_number)
        Camera.__init__(self,megapixels)
        self.model_name = model_name

    def show_info(self) :
        print(f"===== {self.model_name} 정보 =====")
        print(f"전화번호 : {self.phone_number}")
        print(f"카메라 성능 : {self.megapixels}만 화소")