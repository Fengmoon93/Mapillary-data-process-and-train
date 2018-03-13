import os
import shutil
#here is the original dir
filepath='images'
#new path
newpath='pickout'
datalist = os.listdir(filepath)
for step,file in enumerate(datalist):
	file_temp = os.path.join(filepath,file)
	shutil.move(file_temp,newpath)
	#control the work
	if step==201:
	    break
