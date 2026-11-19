https://mirror.akane.netwimport requests 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
class Filedownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("filedownloader")
        """
        ui setup
        """
        self.lblurl = ttk.Label(text="enter a url")
        self.lblurl.grid(column=0,row=0)
        self.txturl = ttk.Entry()
        self.txturl.grid(column=1,row=0)
        self.filetxt = ttk.Entry()
        self.filetxt.grid(column=1,row=1)
        self.filelbl = ttk.Label(text="filename")
        self.filelbl.grid(column=0,row=1)
        
        
        self.btndownload = tk.Button(text="download",command=self.download)
        self.btndownload.grid(column=0,row=5)

        self.progress = ttk.Progressbar(
            orient="horizontal",
            length=300,
            mode="determinate",
            maximum=100
        )
        self.progress.grid(column=0,row=6,columnspan=2,pady=(10,0))

    def download(self):
        """
        this function downloads a file to the hard drive
        """
        try:
            self.url = self.txturl.get()
            self.file = requests.get(str(self.url), stream=True)
            self.file.raise_for_status()

            total = int(self.file.headers.get("content-length", 0))
            downloaded = 0
            self.progress["value"] = 0

            if total > 0:
                self.progress.configure(mode="determinate", maximum=total)
            else:
                self.progress.configure(mode="indeterminate")
                self.progress.start(10)

            with open(str(self.filetxt.get()),"wb") as data:
                for chunks in  self.file.iter_content(chunk_size=8192):
                    data.write(chunks)
                    downloaded += len(chunks)
                    if total > 0:
                        self.progress["value"] = downloaded
                    self.update_idletasks()

            if total > 0:
                self.progress["value"] = total
            else:
                self.progress.stop()
                self.progress.configure(mode="determinate", maximum=100)
                self.progress["value"] = 100
        except requests.exceptions.RequestException as error:
            self.progress.stop()
            self.progress.configure(mode="determinate", maximum=100)
            self.progress["value"] = 0
            messagebox.showerror("",str(error.request))


app = Filedownloader()
app.mainloop()
