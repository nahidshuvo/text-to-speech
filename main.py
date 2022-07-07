import pyttsx3
import PyPDF2
read = open('report.pdf', 'rb' )
pdfReader = PyPDF2.PdfFileReader(read)
speaker = pyttsx3.init()
for num in range(0, 111):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()