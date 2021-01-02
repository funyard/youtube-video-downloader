import os, pytube, keyboard, sys, re, time

video_seznam = []
uporabnik = input("Vnesi ime tvojega profila na windowsu (pojdi pod " + r"C:\\Users\'Ime tvojega profila'): ")
tip_datoteke = input("\nKatere vrste datoteke želiš (mp3 ali mp4)? ")

if tip_datoteke == "mp3":
    print("Vnesi URL-je video-v (Ustavi z 'STOP')")
    while 3 > 2:
        url = input("Vnesi URL: ")
        if url == "STOP":
            break
        video_seznam.append(url)
    print("\n")

    for x, video in enumerate(video_seznam):
        x += 1
        print(f"Nalaganje videa {x} od " + str(len(video_seznam)) + "...")
        v = pytube.YouTube(video)
        v.streams.filter(type = "audio", abr = "128kbps").first().download(f"C:/Users/{uporabnik}/Downloads")
        filename = str(v.title)
        filename = re.sub("[/\.|'#]", "", filename)
        try:
            mp3file = str(f"C:/Users/{uporabnik}/Downloads/{filename}.mp4")
            base = os.path.splitext(mp3file)[0]
            os.rename(mp3file, base + ".mp3")
            print(f"Nalaganje videa {x} od " + str(len(video_seznam)) + " je dokončano.\n")
        except:
            FileNotFoundError
            mp3file = str(f"C:/Users/{uporabnik}/Downloads/{filename}.webm")
            base = os.path.splitext(mp3file)[0]
            os.rename(mp3file, base + ".mp3")
            print(f"Nalaganje videa {x} od " + str(len(video_seznam)) + " je dokončano.\n")

elif tip_datoteke == "mp4":
    print("Vnesi URL-je video-v (Ustavi z 'STOP')")
    while 3 > 2:
        url = input("Vnesi URL: ")
        if url == "STOP":
            break
        video_seznam.append(url)

    for x, video in enumerate(video_seznam):
        x += 1
        print(f"Nalaganje videa {x} od " + str(len(video_seznam)) + "...")
        v = pytube.YouTube(video)
        v.streams.filter(file_extension='mp4').first().download(f"C:/Users/{uporabnik}/Downloads")
        filename = str(v.title + ".mp4")
        print(f"Nalaganje videa {x} od " + str(len(video_seznam)) + " je dokončano.\n")


input("\n\nZa izhod pritisni 'ENTER'.")
print("Zapiranje programa...")
time.sleep(1)
sys.exit()
