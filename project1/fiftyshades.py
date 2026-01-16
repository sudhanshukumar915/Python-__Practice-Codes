import os

command=input("Which Part Do you want to play(Fifty shades of gray, Fifty shades of Freed, Fifty shades of darker)\n Enter Gray,Darker or Freed ?  \n").lower()

if command=="gray":
    print("Playing Fifty Shades of Gray...")
    os.startfile("E:\WEB SERIES IN HOLLYWOOD\Fifty.Shades.of.Grey.2015.1080p.Hindi.English.Vegamovies.NL.mkv")

elif command=="freed":
    print("Playing Fifty Shades of Freed...")
    os.startfile("E:\WEB SERIES IN HOLLYWOOD\2_Fifty.Shades.Freed.2018.1080p.BRRip.Hindi.Dual-Audio.Vegamovies.NL.mkv")

elif command == "darker":
    print("Playing Fifty Shades of darker...")
    os.startfile("E:\WEB SERIES IN HOLLYWOOD\Fifty.Shade.Darker.(2017).1080p.(Hindi.English).Vegamovies.NL.mkv")

else:
    pass