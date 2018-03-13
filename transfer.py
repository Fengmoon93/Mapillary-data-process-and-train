#the code is used for transfering the images in the pickout into Images
import os
import shutil
#here is the original dir
filepath='pickout'
#new path
newpath='Images'
datalist = os.listdir(filepath)
for step,file in enumerate(datalist):
    file_temp = os.path.join(filepath,file)
    shutil.move(file_temp,newpath)

