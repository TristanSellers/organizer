import os  
import shutil

current_dir = os.getcwd()

for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)
    print(filename, file_ext)
    
    try:
        if not file_ext:
            pass
        #Python files
        elif file_ext in ('.py'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Python files', f'{filename}{file_ext}')
            )
        #Image files   
        elif file_ext in ('.jpg', '.png', '.gif'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Image files', f'{filename}{file_ext}')
            )
        #Excel files 
        elif file_ext in ('.xls', '.xlsx', '.xltx', '.xlsm'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Excel files', f'{filename}{file_ext}')
            )
        #Video files
        elif file_ext in ('.mpg'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Video files', f'{filename}{file_ext}')
            )
        #Other files 
        else:
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Other files', f'{filename}{file_ext}')
            )
        
    except (FileNotFoundError, PermissionError):
        pass
    