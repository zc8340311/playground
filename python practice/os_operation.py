import os
import time
today=time.strftime('%Y%m%d')
current_dir=os.getcwd()
destination_dir=r'C:/test_backup'
if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)
if current_dir!=destination_dir:
    os.chdir(destination_dir)

