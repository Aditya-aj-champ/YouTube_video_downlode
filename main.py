## import You Tub from pytube

from pytube import YouTube

print("\nWelcome To python programme for download YouTube videos & Audio ")
print("*******************************************************************")
# plz provide the link from the youtube URL.
link= input("plz provide link of YouTube :-- ")
check = input("what do you want to download press \npress 1 for videose\npress 2 for Audio\nPlz Enter Your choice :- ")
print("Plz wait...... \n")
if check =="1":
    youtube_1 = YouTube(link)
    videos = youtube_1.streams.filter(progressive= True)

    for i,v in enumerate(videos):
        print(f"Press {i} for {v}")
    strm = int(input("Plz provide your index you want to download :-- "))

    print("Plz wait downloading under process...... \n")
    videos[strm].download()
    
    print(" Download Successfully")

if check == "2":
    youtube_1 = YouTube(link)
    aud = youtube_1.streams.filter(only_audio=True)
    for i,v in enumerate(aud):
        # print(i,v)
        print(f"Press {i} for {v}")
    strm = int(input("plz tel us the the index "))
    print("Plz wait downloading under processing...... \n")
    aud[strm].download()
    print(" Download Successfully\n\n")
