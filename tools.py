import os


def changeFileName(path, targetName):
    fileNames = os.listdir(path)
    i = 1
    for name in fileNames:
        src = os.path.join(path, name)
        dst = targetName + str(i) + '.jpg'
        dst = os.path.join(path, dst)
        os.rename(src, dst)
        i += 1
