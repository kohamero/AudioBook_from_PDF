import pyttsx3 # imports tts
import PyPDF2 # imports pdf processing libary to open and read pdfiles
from tkinter.filedialog import * # imports folder tools to select file

book = askopenfilename() # Pop up window to select file
pdfreader = PyPDF2.PdfReader(book) # Feeds that file path into the PDF engine to open and parse the document
pages = len(pdfreader.pages) # Count number of pages
player = pyttsx3.init() # initializes the audio engine

for num in range(0, pages): # Num = 0 at start ++ at end of each loops
    page = pdfreader.pages[num] # takes page no.num
    text = page.extract_text() # extracts text 
    player.say(text) # adds text to audio queue
    player.runAndWait() # say text out loud and waits until done