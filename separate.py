import os,scan,shutil
folderpath=input("enter the name of your foldername with double slash\n")
data=dict()
data['audiofile']=scan.audio_scan(folderpath)
data['videofile']=scan.video_scan(folderpath)
data['documentfile']=scan.document_scan(folderpath)
data['imagefile']=scan.image_scan(folderpath)
for fileType in data.keys():
    if data[fileType]:
        x=len(data[fileType])
        print("there are "+ str(x)+" "+str(fileType))
        print("do you want to move the  "+str(fileType)+"  yes\no?")
        x=input()
        if(x=='yes'):
              print("for move the"+" "+str(fileType)+" "+"type the new folder name")
              while True:
                  foldername=input()
                  newfolderpath=os.path.join(folderpath,foldername)
                  if os.path.isdir(newfolderpath):
                           print("this folder is alreday exist")
                           continue
                  else:
                     os.makedirs(newfolderpath)
                  break
              for file in data[fileType]:
                        currentpath=os.path.join(folderpath,file)
                        destinationpath=os.path.join(newfolderpath,file)
                        shutil.move(currentpath,destinationpath)
        else:
            print("user not want to move the file")
              
    else:          
       print("sorry there is no any "+str(fileType))
              
                   
              
              
              
