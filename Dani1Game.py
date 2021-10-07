import tkinter as tk
import os
import playsound
from gtts import gTTS
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def readme():
	tts = gTTS(text =narr["text"], lang='en')
	filename="DaniTemp.mp3"
	tts.save(filename)    
	playsound.playsound(filename)
	os.remove(filename)

def yesf():
	narr.configure({"text":"You've left \n Do you grab the hammer?"})
	btn_yes.configure(command=hammeryes)
	btn_no.configure(command=hammerno)

	readme()


def hammerno():
	narr.configure({"text":"Do you want to go back in?"})
	btn_yes.configure(command=surecheckyes)
	btn_no.configure(command=leftcheckno)

	readme()

def hammeryes():
	narr.configure({"text":"Go back in?"})
	btn_no["state"] = "disabled"
	btn_yes.configure(command=kill)

	readme()

def kill():
	narr.configure({"text":"You come back in just in time\n to see someone crawling in.\n You bring the hammer down upon their head"})
	btn_yes["state"] = "disabled"
	btn_no["state"] = "disabled"

	readme()

def leftcheckno():
	narr.configure({"text":"You leave without incident. \n B O R I N G"})
	btn_yes["state"] = "disabled"
	btn_no["state"] = "disabled"

	readme()

def nof():
	narr.configure({"text":"You stay. Are you sure?"})
	btn_yes.configure(command=surecheckyes)
	btn_no.configure(command=yesf)

	readme()

def surecheckyes():
	narr.configure({"text":"A serial killer came in through the window \n and murdered you brutally."})
	btn_yes["state"] = "disabled"
	btn_no["state"] = "disabled"

	readme()

def rstf():
	narr.configure({"text":"You are in a room. Do you wish to leave?"})
	btn_yes["state"] = "normal"
	btn_no["state"] = "normal"
	btn_yes.configure(command=yesf)
	btn_no.configure(command=nof)

	readme()

   

window = tk.Tk()
window.title("Dani's Game")

narr = tk.Label(height=20, width=40, text="You are in a room. Do you wish to leave?", relief=tk.SUNKEN, fg="black", bg="white")
narr.pack(side=tk.TOP)

btn_yes = tk.Button(height=5, width=10, text="Yes", padx=10, master=window, relief=tk.GROOVE, command=yesf)
btn_yes.pack(side=tk.LEFT)

btn_no = tk.Button(height=5, width=10, text="No", padx=10, master=window, relief=tk.GROOVE, command=nof)
btn_no.pack(side=tk.LEFT)

btn_rst = tk.Button(height=5, width=10, text="Restart", padx=10, master=window, relief=tk.GROOVE, command=rstf)
btn_rst.pack(side=tk.LEFT)

readme()

window.resizable(False,False)
window.wm_iconbitmap('Danicon3.ico')
window.mainloop()