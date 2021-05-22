import pdftotext
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("PDF convert to TXT")
window.geometry("400x120")
window.call("wm", 'iconphoto', window._w, PhotoImage(file="ico.png"))
x = ""

def openfile():
	window.title('file_select')
	window.filename = filedialog.askopenfilename(initialdir='~/', title = "Select PDF",filetypes = (("PDF files","*.pdf"),("all files","*.*")))
	global x
	x = window.filename

def start():
	txtnameIn = txtname.get()
	with open(x, "rb") as f:
		pdf = pdftotext.PDF(f)
	
	# Save all text to a txt file.
	with open('%s.txt'%txtnameIn, 'w') as f:
		f.write("\n\n".join(pdf)) 

Label(window, font='monospace 9 italic', text='PDF file: ').place(x=10, y=10, anchor=NW)
Label(window, font='monospace 9 italic', text='TXT Name: ').place(x=10, y=40, anchor=NW)

txtname = Entry(window, font='monospace 9')

txtname.place(x=100, y=40, bordermode=INSIDE, width=258)


Button(window, text='PDF-file', command=openfile).place(x=100, y=5)
Button(window, text='Start', command=start).place(x=300, y=80)
Button(window, text='Quit', command=window.quit).place(x=50, y=80)

window.mainloop()





#Debian, Ubuntu, and friends
#sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev

#Fedora, Red Hat, and friends
#sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel

#macOS
#brew install pkg-config poppler python

#Windows
#    conda install -c conda-forge poppler

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Install
#pip install pdftotext

