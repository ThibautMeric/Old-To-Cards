try:
    import tkinter as tk
    from tkinter.filedialog import *
    import tkinter.ttk as ttk
    import tkinter.messagebox
except:
    import Tkinter as tk
    from tkFileDialog import *
    import ttk as ttk
    import tkMessageBox
    from Tkinter import *
from Old_To_Cards.Others.Reset import *
from Old_To_Cards.Step3.Generate import *
import platform

def InitializeStep3(lfStep1, lfStep2, lfStep3, WindowSetting, Version, HtmlPath, HtmlTable):

    #Definition for Step 3
    CallGenerate = lambda: Generate(HtmlPath, HtmlTable, lfStep2)
    if(platform.system() == 'Windows'):Gen = ttk.Button(lfStep3, text="Generate", command=CallGenerate, width=int(15 * WindowSetting["Reduce"]), name="generate")
    else:Gen = tk.Button(lfStep3, text="Generate", command=CallGenerate, width=int(15 * WindowSetting["Reduce"]), name="generate")

    Callreset = lambda: Reset( lfStep1, lfStep2, lfStep3, HtmlPath, HtmlTable, WindowSetting)
    if(platform.system() == 'Windows'):Rst = ttk.Button(lfStep3, text="Select new files", command=Callreset, width=int(15 * WindowSetting["Reduce"]), name="reset")
    else:Rst = tk.Button(lfStep3, text="Select new files", command=Callreset, width=int(15 * WindowSetting["Reduce"]), name="reset")
pass
