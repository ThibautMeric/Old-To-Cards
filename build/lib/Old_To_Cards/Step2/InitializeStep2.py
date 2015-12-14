try:
    import tkinter as tk
except:
    import Tkinter as tk
    from Tkinter import *
def InitializeStep2(lfStep2):
    TitleStep2 = tk.Label(lfStep2, text="Set the correct equivalent in Bootstrap 4:", name="titlestep2")

    lfPanel = tk.LabelFrame(lfStep2, text="Panel:", name ="lfpanel")
    lfThumbnail = tk.LabelFrame(lfStep2, text="Thumbnail:",name ="lfthumbnail")
    lfWell = tk.LabelFrame(lfStep2, text="Well:",name ="lfwell")
pass