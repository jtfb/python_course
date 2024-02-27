import shutil
import re
import os

# os.getcwd()
# os.listdir("C:\\Users")

# shutil.move("practice.txt","C:\\Users\\tiagofoa")

# shutil.unpack_archive('C:\\Users\\TIAGOFOA\\Desktop\\PYTHON\\EXERCISES\\ZIP_AND_UNZIP\\unzip_me_for_instructions.zip','C:\\Users\\TIAGOFOA\\Desktop\\PYTHON\\EXERCISES\\ZIP_AND_UNZIP\\','zip')

# with open("C:\\Users\\TIAGOFOA\\Desktop\\PYTHON\\EXERCISES\\ZIP_AND_UNZIP\\extracted_content\\Instructions.txt") as f:
#     content = f.read()
#     print(content)

def search(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ""
        
results = []
for folder,subfolders,files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        full_path = folder+'\\'+f
        
        results.append(search(full_path))
      
for r in results:
    if r != "":
        print(r.group())  