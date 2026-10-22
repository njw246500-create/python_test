'''
* package : 관련있는 파이썬 파일(모듈)들을 기능별로 분류하여 모아놓은 디렉토리
    패키지 안에는 __init__.py라는 파일이 있음

* __init__.py
    - 파이썬 패키지(구조화된 모듈 모음)라고 파이썬 시스템에 알려주는 역할
        > 파이썬 2에서는 이 파일이 없으면 패키지로 인식못함
        > 파이썬 3부터는 이 파일이 없어도 패키지로 인식 
        > 실무에서는 이 파일을 넣는것을 권장
    - 기능
        1. 패키지를 불러올 때 가장 먼저 자동 실행(초기화) 닥 한번 실행
            > 패키지를 쓰기 전에 미리 설정해야 되는 것들. 
                ex) 데이터베이스 연결, 로그 기록 설정, 환경변수 로드 등의 초기화 작업시 작성
        2. 패키지 가져오기(import) 경로 단축
        3. 패키지 내의 비밀파일등의 목록을 지정해 둘 수 있다.
            > 호출시 from package import * 
            > __all__ 변수에 공개할 파일 목록만 지정 가능 

'''

# 1
import package01.image.io_file.imgRead
package01.image.io_file.imgRead.jpgRead()
package01.image.io_file.imgRead.pngRead()

import package01.image.io_file.imgSave
package01.image.io_file.imgSave.jpgSave()
package01.image.io_file.imgSave.pngSave()
print('-'*30)

# 2
import package01.image.io_file.imgRead as ir
import package01.image.io_file.imgSave as ims

ir.pngRead()
ir.jpgRead()

ims.jpgSave()
ims.pngSave()
print('-'*30)

# 3
from package01.image.io_file import imgRead
imgRead.jpgRead()
imgRead.pngRead()
print('-'*30)

# 4
from package01.image.io_file import imgRead as imr
imr.jpgRead()
imr.pngRead()
print('-'*30)

# 5
from package01.image.io_file.imgRead import pngRead, jpgRead
pngRead()
jpgRead()
print('-'*30)

# 6 
from package01.image.io_file.imgRead import pngRead as pr
from package01.image.io_file.imgRead import jpgRead as jr
pr()
jr()