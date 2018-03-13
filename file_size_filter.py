#here is the code for delete the file that is less tha 650 kb
import os
import shutil
filepath='Images'
datalist = os.listdir(filepath)
print('there are {:d} files'.format(len(datalist)))
for step,file in enumerate(datalist):
    single_file = os.path.join(filepath,file)
    #here return the size of the file in "KB"
    size=os.path.getsize(single_file)/1024
    if size<700:
        print('the file is {:s},the data size is {:.2f} kb,remove it...'.format(single_file,size))
        os.remove(single_file)

