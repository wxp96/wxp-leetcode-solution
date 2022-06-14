import os

if __name__=="__main__":
    path=os.getcwd()
    #print(path)
    filelist=os.listdir(path)
    for fileordir in filelist:
        if os.path.isdir(fileordir):
            continue
        if fileordir.split('.')[0].split('_')[-1].isdigit():
            new_name=fileordir.split('.')[0].split('_')[-1]+'_'+fileordir.rsplit('_',1)[0]+".py"
            # print(new_name)
            os.rename(fileordir,new_name)