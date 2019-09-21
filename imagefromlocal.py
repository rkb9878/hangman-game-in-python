import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
root.title("display image")
im=Image.open("D:/1.jpg")  #This is the correct location and spelling for my image location
photo=ImageTk.PhotoImage(im)
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(10, 10, image=photo, anchor='nw')
root.mainloop()