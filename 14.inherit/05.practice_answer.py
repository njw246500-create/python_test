'''
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

## test 하기

if __name__=='__main__' :
    my_phone = SmartPhone('010-1234-1234', 2000, 'Galaxy Ultra')

    my_phone.show_info()

    my_phone.call('010-5678-9012') 

    my_phone.take_photo()'''

from smartPhone import SmartPhone #smartPhone 파일에서 class SmartPhone 을 가지고 오겠다 

# 다중상속 파일이라서 다중상속인거를 불러오면 부모도 같이 불러와지게된다. 부모 아니면 옆에 콤마하고 import 에 추가해야함. 

my_phone = SmartPhone('010-1234-1234', 2000, 'Galaxy Ultra')

my_phone.show_info()

my_phone.call('010-5678-9012') 

my_phone.take_photo()
