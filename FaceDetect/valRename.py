import os
foo = open("val.txt", "w")

path1 = r"C:\Users\taros\FaceDetect\val\acne"
path2 = r"C:\Users\taros\FaceDetect\val\norm"
i = 1
j = 1
for file in os.listdir(path1):
    newname='acne_%d.jpeg'%i
    os.rename(os.path.join(path1,file),os.path.join(path1,newname))
    foo.write("/acne/"+newname+" 0\n")
    i += 1
for file in os.listdir(path2):
    newname='norm_%d.jpeg'%j
    os.rename(os.path.join(path2,file),os.path.join(path2,newname))
    foo.write("/norm/"+newname+" 1\n")
    j += 1
