print('------ 1. 패키지 불러오기 시작 -----')
from package02 import module1

print('------ 1. 패키지 불러오기 완료 -----')
module1.run_function()

# from package02.image.io_file.imgRead import pngRead, jpgRead
import package02 as p2
# package02.jpgRead()
# package02.pngRead()
p2.jpgRead()
p2.pngRead()


