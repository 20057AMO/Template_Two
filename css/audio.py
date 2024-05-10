from pytube import YouTube
try:
    link = str(input("Insert Youtube Link : "))
    path = str(input("\nWriter Path File : "))

    print("\nLoding...."),YouTube(link).streams.get_audio_only().download(path)
    print("\nCompelte...")
except Exception as E :
    print(f"Error!! {E}")    