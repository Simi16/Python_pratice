#In this program, only use if-elif-else a basic menu to complete this task and it is design for windows base os.
#Menu Run For Base Operating System:
import os
print("Hello This is the windows chatbox:")
while True:
  print("Chat With Me with Your Requirement: ", end='')
  p=input()
  if (("open" in p) or ("run" in p) or ("start" in p) or ("launch" in p) or ("execute" in p)) and (("notepad" in p) or ("text editior" in p) or ("editior" in p)):
    os.system("notepad")
  elif (("open" in p) or("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p)) and ("calculator" in p):
    os.system("calc")
  elif (("open" in p) or("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p)) and (("chrome" in p) or ("google chrome" in p)):
    os.system("chrome")
  elif (("open" in p) or("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p)) and (("browser" in p) or ("internet explore" in p) or ("explore" in p)):
    os.system("start iexplore")
  elif (("open" in p) or ("start" in p)) and ("control panel" in p):
    os.system("control")
  elif (("open" in p) or ("start" in p))and ("camera" in p):
    os.system("start microsoft.windows.camera:")
  elif (("open" in p) or("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p)) and ("sublime text" in p):
    os.system("sublime_text")
  elif (("open" in p) or ("start" in p)) and (("microsoft word" in p) or ("word" in p)):
    os.system("start winword")
  elif (("open" in p) or ("start" in p)) and (("adobe reader" in p) or ("adobe" in p)):
    os.system("AcroRd32")
  elif (("open" in p) or ("start" in p)) and (("windows media player" in p) or ("media player" in p)):
    os.system("wmplayer")
  elif(("open" in p) or ("start" in p)) and (("vlc" in p) or ("video player" in p)):
    os.system("vlc")  
  elif (("open" in p) or ("start" in p)) and (("microsoft excel" in p) or ("excel" in p)):
    os.system("start excel")
  elif (("open" in p) or ("start" in p)) and (("wordpad" in p) or ("word" in p)):
    os.system("write")
  elif (("open" in p) or ("start" in p)) and (("microsoft powerpoint" in p) or ("powerpoint" in p)):
    os.system("powerpnt")
  elif (("open" in p) or ("start" in p)) and (("microsoft oneNote" in p) or ("notebook" in p)):
    os.system("onenote")
  elif (("open" in p) or ("start" in p)) and (("microsoft outlook" in p) or ("outlook" in p)):
    os.system("outlook")
  elif (("open" in p) or("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p)) and ("skype" in p):
    os.system("skype")
  elif (("start" in p ) or ("open" in p)) and ("stiky note" in p):
     os.system("stikynot")
  elif (("start" in p) or ("open" in p)) and (("paint brush" in p) or ("paint" in p) ):
     os.system("mspaint")
  elif(("start" in p) or ("open" in p)) and ("weather" in p):
     os.system("start bingweather:")
  elif(("start" in p) or ("open" in p)) and ("setting" in p):
     os.system("start ms-settings:")
  elif(("start" in p) or ("open" in p)) and (("mail" in p) or ("email" in p)):
     os.system("start outlookmail")
  elif(("start" in p) or ("open" in p)) and (("message" in p) or ("chat" in p)):
     os.system("start ms-chat")
  elif(("start" in p) or ("open" in p)) and (("store" in p) or ("microsoft store" in p)):
     os.system("start ms-windows-store:")
  elif (("start" in p) or("open" in p)) and ("calender" in p):
    os.system("outlookcal:") 
  elif(("exit" in p) or ("quit" in p) or("end" in p) or ("close" in p)):
    print("Thank You")
    break
  else:
    print("dont support")