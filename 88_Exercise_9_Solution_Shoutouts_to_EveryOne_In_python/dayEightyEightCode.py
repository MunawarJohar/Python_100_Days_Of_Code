import win32com.client as win
speak=win.Dispatch("SAPI.SpVoice")

names=["Munawar","MarZi@","Harry","Kamal","Ali","Raziq","Munawar Johar","Marzia","Sharif","Alam","Hanif"]
# print the names
for name in names:
    print(f"Shoutout to "+name)
# for speak the names   
for names in names:
    speak.Speak(f"Shoutout to {names}")