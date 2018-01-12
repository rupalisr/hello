import os
def audio_scan(folderpath):
    audios=[]
    audiofiles=os.listdir(r"E:\song2")
    audioExtensions=['mp3','flac','aa','mp4a','aac','.mp3']
    for audioExtension in audioExtensions:
        for allfiles in audiofiles:
            if audioExtension in allfiles:
                audios.append(allfiles)
    return audios                
def video_scan(folderpath):
    videos=[]
    videofiles=os.listdir(r"E:\song2")
    videoExtensions=['mp4','mpeg','avi','mkv','.mp4']
    for videoExtension in videoExtensions:
        for allfiles in videofiles:
            if videoExtension in allfiles:
                videos.append(allfiles)
  
    return videos
def image_scan(folderpath):
    images=[]
    imagefiles=os.listdir(r"E:\song2")
    imageExtensions=['jpeg','png','gif','JPEG','.jpg']
    for imageExtension in imageExtensions:
        for allfiles in imagefiles:
            if imageExtension in allfiles:
                images.append(allfiles)
    return images
def document_scan(folderpath):
    documents=[]
    documentfiles=os.listdir(r"E:\song2")
    documentExtensions=['.docx','pdf','.txt','.doc','.xlsx']
    for documentExtension in documentExtensions:
        for allfiles in documentfiles:
            if documentExtension in allfiles:
                documents.append(allfiles)
    return documents


