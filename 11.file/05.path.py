from pathlib import Path

target_file = Path('./11.file/output/result_data.txt')

target_file.parent.mkdir(parents = True, exist_ok = True)

with open(target_file,'w') as f: 
    f.write('성공적으로 저장')