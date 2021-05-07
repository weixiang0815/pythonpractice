from pytube import YouTube

# link = input("Enter the link of the video: ")
link = "https://www.youtube.com/watch?v=of-WFfQ8MsU&list=WL&index=9"
yt = YouTube(link)

print("Title: " + yt.title)
print("Author:" + yt.author)
print("Views: " + str(yt.views) + " views")
print("Rating: " + str(round(yt.rating, 1)))

# time calculating
if yt.length < 60:
    print("Length: " + str(yt.length) + " seconds")
else:
    secs = yt.length % 60
    mins = int(yt.length / 60)
    if yt.length < 3600:
        print("Length: " + str(mins) + " minutes " + str(secs) + " seconds")
    else:
        hrs = int(yt.length / 3600)
        if yt.length < 3600 * 24:
            print("Length " + str(hrs) + " hours " + str(mins) + " minutes " + str(secs) + "seconds")
        else:
            days = int(yt.length / (3600 * 24))
            print("Length " + str(days) + " days " + str(hrs) + " hours " + str(mins) + " minutes " + str(
                secs) + "seconds")

checkDescription = input("Do you want to read the description?(y/n) ")
if checkDescription.lower() == 'y':
    print("Description:")
    print(yt.description + "\n")

# streams printing manipulation
checkAS = input("Which kind of Available Streams would you like to check out?(video/audio/all) ")
i = 0
if checkAS.lower() == 'video':
    print("Available Video Streams:")
    for x in yt.streams.filter(only_video=True):
        print(yt.streams.filter(only_video=True)[i])
        i += 1
elif checkAS.lower() == 'audio':
    print("Available Audio Streams:")
    for x in yt.streams.filter(only_audio=True):
        print(yt.streams.filter(only_audio=True)[i])
        i += 1
elif checkAS.lower() == 'all':
    print("Available Streams:")
    for x in yt.streams:
        print(yt.streams[i])
        i += 1
print()

# downloading process
checkPRG = input("Would you like to check out the progressive streams of the video?(y/n) ")
if checkPRG.lower() == 'y':
    i = 0
    for x in yt.streams.filter(progressive=True):
        print(yt.streams.filter(progressive=True)[i])
        i += 1
else:
    print("Alright! Let's skip to the download process then!")
print()

getTag = input("Which stream of the video would you like to download?(the highest resolution/the available tag) ")
if getTag.lower() == 'the highest resolution':
    yt.streams.get_highest_resolution().download()
else:
    yt.streams.get_by_itag(int(getTag)).download()
print("Please wait. This may take a while.")
print()

# finished
print("The process is completed.")
print("Go ahead and check out your download!")
