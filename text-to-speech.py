from gtts import gTTS

print("witaj w naszej aplikacji ktora zamienia tekst na mowe")
print("wpisz zdanie ktore chcesz zamienic na tekst")
slowo = input()
print("po angielsku czy po polsku?")
jezyk = input()

if jezyk == "polsku":
    cos = gTTS(slowo)
    cos.save("plikPL.mp3")
elif jezyk == "angielsku":
    cos = gTTS(slowo)
    cos.save("plikENG.mp3")