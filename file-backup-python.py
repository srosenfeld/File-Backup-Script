import shutil
import time
import socket

#get username
hostname = socket.gethostname()

# dd/mm/yyyy format
date = str(time.strftime("%d-%m-%Y"))

# C:/Users/ should be replaced with the directory you want to save to
filename = 'C:/Users/' + date + '.xlsx'

# C:/Users/original.xlsx should be replaced with file you want to back up
shutil.copy2('C:/Users/original.xlsx', filename
