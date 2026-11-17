import requests 
import tkinter as tk
from tkinter import messagebox
class Filedownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("filedownloader")
        """
        ui setup
        """
        self.lblurl = tk.Label(text="enter a url")
        self.lblurl.grid(column=0,row=0)
        self.txturl = tk.Entry()
        self.txturl.grid(column=1,row=0)
        self.filetxt = tk.Entry()
        self.filetxt.grid(column=1,row=1)
        self.filelbl = tk.Label(text="filename")
        self.filelbl.grid(column=0,row=1)
        
        
        self.btndownload = tk.Button(text="download",command=self.download)
        self.btndownload.grid(column=0,row=5)
    def download(self):
        """
        this function downloads a file to the hard drive
        """
        try:
            self.url = self.txturl.get()
            self.file = requests.get(str(self.url))
            self.file.raise_for_status()

            with open(str(self.filetxt.get()),"wb") as data:
                for chunks in  self.file.iter_content(chunk_size=8192):
                    data.write(chunks)
        except requests.exceptions.RequestException as error:
            messagebox.showerror("",str(error.request))


app = Filedownloader()
app.mainloop()