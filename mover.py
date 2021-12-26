from pathlib import Path
import shutil
import os

src_path ='C:/Users/Ronnie Atuhaire/Downloads/'
trg_path ='C:/Users/Ronnie Atuhaire/Downloads/Mine'

extensions = ['.png', '.jpeg', 'jpg', 'gif', 'tiff', 'jfif', 'ico']

for src_file in Path(src_path).glob('*.pdf*'):
    try:
        shutil.move(os.path.join(src_path,src_file),trg_path)
    except:
        pass
