import pywhatkit
x=input("what dou want to do ")
if x=='whatsapp':
    y=input('enter the phone number u want to message ')
    msg=input('enter the message ')
    ti=int(input('enter the hour in 24 hr format'))
    tim=int(input('enter the min '))
    pywhatkit.sendwhatmsg(y,msg,ti,tim)
elif x=="yt":
    play=input('enter a song')
    pywhatkit.playonyt(play)