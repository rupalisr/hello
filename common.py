import os
song1path=r"E:\python\Songs"
song1=os.listdir(song1path)
song2path=r"E:\python\Songs\old songs"
song2=os.listdir(song2path)
for song in song1:
    if song in song2:
        commonsong=os.path.join(song2path,song)
        os.remove(commonsong)

