import pyttsx3 #terminal command pip install pysttx3
import PyPDF2  #terminal command pip install 'pyPDF2<3.0' 
from tkinter.filedialog import *

book = askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book) 
pages=pdfreader.numPages

for num in range(0,pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait() 
