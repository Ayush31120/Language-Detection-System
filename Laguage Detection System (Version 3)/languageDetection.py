# Ayush Mishra
# Masters of Computer Application

# Date 16 July 2023

"""
Language Detection System GUI (Graphical User Interface)
This is The project which is used for detecting a language by following inputs:
1. Text
2. Image
3. Voice

Modules Used in this project is:
1. Tkinter      ----    Tkinter module in python to create GUI (Graphical User Interface) based 
                        interface.

2. langdetect   ----    We are using langdetect module. langdetect module is a port of Google's
                        language- detection library that supports 55 languages. This modules 
                        doesn't come with Python's standard utility modules. So it is needed to 
                        install it externaly. 
                        Following command for installation:
                        pip install langdetect

3. iso-639      ----    The detected language will give output in code like en for english to
                        solve this issue we will use iso-639 module to give language name for
                        their respective detected language.
                        Following command for installation:
                        pip install iso-639

4. Speech_recognition   The SpeechRecognition module depends on pyaudio.
                        Following Command for installation
                        pip install SpeechRecognition

5. file_dialog  ----    It is Used for opening and saving file. It is part of tkinter.

6. pytesseract  ----    Tesseract is an optical character recognition engine for various operating 
                        systems. It is free software, released under the Apache License. 
                        It is based on LSTM.

7. PIL          ----    The Python Imaging Library adds image processing capabilities to your 
                        Python interpreter.
"""

# Importing Modules

from tkinter import*             #Tkinter for GUI
from langdetect import*          #langdetect for language detaction
from iso639 import languages     #To detect code of language
from tkinter import messagebox   #For Message box
import speech_recognition as sr  #For Speech Detection
from tkinter import filedialog   #For Opening File 
import pytesseract               #For Reading Image Text
from PIL import Image            #For Image Processing

#Path to tesseract Executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Creating GUI Object
root = Tk()

# Title of Window
root.title("Language Detection")

#icon of Window
icon1 = PhotoImage(file="Laguage Detection System (Version 3)/icon.png")
root.iconphoto(False, icon1)

#Setting size of window
root.geometry("500x640")

# Creating funcition to use in text language detection
def language_detection():
    text = t.get("1.0",'end-1c')

    #Getting language code
    language_code = languages.get(alpha2=detect(text))
    messagebox.showinfo("Detected ",language_code.name)

# Creating Function for Speech
def sLanguage_detection():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speek anything: ") 
        audio = r.listen(source)
        try:
            au = r.recognize_google(audio)
            language_code = languages.get(alpha2=detect(au))
            messagebox.showinfo("Detected ",language_code.name)
        except:
            messagebox.showerror("Error","Cant Hear You")

# Creating Function for Image
def iLanguage_detection():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        image = Image.open(file_path)
        textimg = pytesseract.image_to_string(image)
        print("Detected Text:", textimg)
        language_code = languages.get(alpha2=detect(textimg))
        messagebox.showinfo("Detected ",language_code.name)
    else:
        messagebox.showerror("Error", "Something Went Wrong")

#Heading Label
headlbl = Label(root, text ="Laguage Detection System")
headlbl.pack(pady=5)
headlbl.config(font=("Consolas",16))

# Creating Text Box
t = Text(root)
t.pack()

# label for text
textlbl = Label(root, text ="Please Click Button To Know Your Language")
textlbl.pack(pady=5)

# Button for text
Button(root, text="Detect Language",command = language_detection).pack(pady=5)

# label for speech
speechlbl = Label(root, text ="Please Click Button To Speek")
speechlbl.pack(pady=5)

# Button for speech
Button(root, text="Speek",command = sLanguage_detection).pack(pady=5)

#label for image
imagelbl = Label(root, text ="Select Your Image")
imagelbl.pack(pady=5)

#Button For Image
Button(root, text="Select Image",command = iLanguage_detection).pack(pady=5)

# Execute Main Loop
root.mainloop()
print("Build succsesful.....\nNo Compilation Error.....")