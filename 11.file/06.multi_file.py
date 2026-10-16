from pathlib import Path 

# 읽어올 폴더 지정
data_dir = Path('11.file/output')

# 폴더 안의 .txt확장자명은 모두 가져오기 
txt_files = data_dir.glob('*.txt') # text 에 해당하는 모든 파일을 변수로 지정함. 

for file in txt_files:
    print(f'=========================== [파일 읽기 : {file.name}] =============================')
    with open(file, 'r') as f : 
        content = f.read()
        print(content)
    print("-"*30)

