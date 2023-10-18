import os
import time
venv = 'nlp'
if os.path.exists(venv):
    os.startfile('')
else:
    venv = 'nlp'
    os.system(f'cmd /c "python -m venv {venv}"')
    dir = os.getcwd()
    dir = dir.replace("\\",'/')
    print(dir)
    time.sleep(2)
    os.system(dir+"/nlp/Scripts/pip.exe install -r requirements.txt")
    time.sleep(5)

    import shutil
    source_dir = r"files"
    destination_dir = r"nlp"
    shutil.copytree(source_dir, destination_dir,dirs_exist_ok=True)
    
    