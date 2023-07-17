# Language-Detection-System
This is the project which can be used to detect Languages by following inputs:
1. Text.
2. Image.
3. Voice.
## Modules-used-in-project:
1. Tkinter------------------------------Tkinter module in python to create GUI (Graphical User Interface) based 
                                        interface.

2. langdetect---------------------------We are using langdetect module. langdetect module is a port of Google's
                                        language- detection library that supports 55 languages. This modules 
                                        doesn't come with Python's standard utility modules. So it is needed to 
                                        install it externaly. 
                                        Following command for installation:
                                        pip install langdetect

3. iso-639------------------------------The detected language will give output in code like en for english to
                                        solve this issue we will use iso-639 module to give language name for
                                        their respective detected language.
                                        Following command for installation:
                                        pip install iso-639

4. Speech_recognition-------------------The SpeechRecognition module depends on pyaudio.
                                        Following Command for installation
                                        pip install SpeechRecognition

5. file_dialog--------------------------It is Used for opening and saving file. It is part of tkinter.

6. pytesseract--------------------------Tesseract is an optical character recognition engine for various operating 
                                        systems. It is free software, released under the Apache License. 
                                        It is based on LSTM.

7. PIL----------------------------------The Python Imaging Library adds image processing capabilities to your 
                                        Python interpreter.
## Maybe a problem
Hindi Detection Doesn't work good sometimes on Speech and Image Otherwise everthing is fine.
## Note-
Downlode and install Pytesseract first and after setting the variable it will work, Otherwise it shows error of Tesseract not found.

## Made by Ayush Mishra
