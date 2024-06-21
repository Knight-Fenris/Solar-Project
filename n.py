import os 

for filename in os.listdir("./labels"):
    if '_' in filename:
        temp = filename.replace('_',' ')
        print(temp[9:])
        os.rename(os.path.join("./labels",filename), temp[9:])