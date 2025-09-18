import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter.simpledialog import*
from tkinter.scrolledtext import ScrolledText
from PIL import Image,ImageTk



class Window(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.geometry = ("300x200")
        self.font = ("arial",9)
        self.title = self.master.title("Sikespad")
        self.pack()
        self.menubar()
        self.work_area()
    def menubar(self):
        men = tk.Menu(self.master)
        file = tk.Menu(men)
        file.add_command(label='Open',command= self.open_file)
        file.add_command(label='Save',command=self.save_file)
        file.add_command(label='Save  As... ',command=self.save_file)
        file.add_command(label='Close',command=self.close)
        file.add_command(label='Exit',command=self.exit)
        edit = tk.Menu(self.master)
        edit.add_command(label='Undo',command= self.undo)
        edit.add_command(label='Redo',command= self.redo)
        edit.add_command(label='Search',command= self.find)
        insert = tk.Menu(self.master)
        insert.add_command(label='image',command= self.insert_image)
        font = tk.Menu(self.master)
        font.add_command(label='Font style',command= self.font_value)
        men.add_cascade(label='File',menu=file)
        men.add_cascade(label="Edit",menu=edit)
        men.add_cascade(label='Insert',menu=insert)
        men.add_cascade(label='Font',menu=font)
        #insert.add_cascade(label='Insert',menu=insert)
        men.config(bg='#00FCAA')
        self.master.config(menu=men)
    def insert_image(self):
    	filename = askopenfilename(filetypes=[("defaultextension","*.png"),("all_files","*.*")])
    	self.show_img(filename)
    def undo(self):
    	try:
    		self.text_box.edit_undo()
    	except:
    		pass
    def redo(self):
    	try:
    		self.text_box.edit_redo()
    	except:
    		pass
    def font_value(self):
       root= tk.Tk()
       root.geometry("640x210")
       root.configure(bg='white')
       root.title("font stlye")
       label = tk.Label(root,text="Enter the font style and size eg.(None,12)")
       label.place(x=10,y=30)
       entry = tk.Entry(root)
       entry.place(x=100,y=100)
       entry.insert(0,self.font)
       btn = ttk.Button(root,text='set',command=lambda : set_value())
       btn.place(x=180,y=150)
       def set_value():
        	val = entry.get()
        	self.font = val
        	root.destroy()
    def show_img(self,img):
       load = Image.open(img)
       render = ImageTk.PhotoImage(load)
       pic = ttk.Label(self,image=render)
       pic.image = render
       pic.place(x=50,y=50)
    def work_area(self):
        self.text_box = ScrolledText(self,width=38,height=35,border=5,wrap="word",font=self.font,bg="#e7fafe",undo=True)
        self.text_box.pack(fill="both",expand=True,anchor="center")
        self.text_box.font = self.font_value()
    def open_file(self):
        filename = askopenfilename()
        filename = str(filename)
        with open(filename,'r') as f:
            self.text_box.delete(0.1,tk.END)
            self.text_box.insert(tk.END,f.read()) 
    def find(self, *args):
        self.text_box.tag_remove('found', '1.0', tk.END)
        target = askstring('Find', 'Search String:')

        if target:
            idx = '1.0'
            while 1:
                idx = self.text_box.search(target, idx, nocase=1, stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(target))
                self.text_box.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text_box.tag_config('found', foreground='white', background='blue')          
            
    def save_file(self):
        filename = asksaveasfilename(filetypes=[("defaultextension","*.txt"),("all_files","*.*")])
        with open(filename,'w') as f:
            content = self.text_box.get(0.1,tk.END)
            f.write(content)
        
        pass
    def exit(self):
        self.master.quit()
    def close(self):
        self.text_box.delete(0.1,tk.END)
        
root = tk.Tk()
app = Window(root)
app.mainloop()