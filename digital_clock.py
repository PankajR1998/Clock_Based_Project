from tkinter import Tk,Label
import time

window = Tk()
window.title('Digital Clock')
window.geometry("480x150")
window.resizable(True,True)

# write it's css.
text_font= ("Boulder", 68, 'bold')
background = "#36393e"
foreground= "#7289da"
border_width = 25


label = Label(window,font=text_font, bg=background,fg=foreground,bd=25)
label.grid(row=100,column=200)

def digital():
    live_time = time.strftime('%H:%M:%S')
    label.config(text=live_time)
    label.after(200,digital)

digital()

window.mainloop()