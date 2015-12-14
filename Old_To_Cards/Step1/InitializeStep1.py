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
import platform
from Step1.OpenHTML import *
from Step1.RefreshStep1 import *
from Step1.EnableAddHTML import *

def InitializeStep1(lfStep1, lfStep2, lfStep3,WindowSetting, HtmlPath, Bottom, HtmlTable, ConversionDict, CardTable):   
    TitleHtml = tk.Label(lfStep1, text="Add an HTML file", name="titlehtml")
    
    CallAddHTML = lambda: AddHTML(lfStep1, WindowSetting, HtmlPath)
    CallAddHTMLForEntry = lambda event: AddHTML(lfStep1, WindowSetting, HtmlPath)
    if(platform.system() == 'Windows'):AddHtml = ttk.Button(lfStep1, text="Add HTML file", command=CallAddHTML, state="disable", width=int(15 * WindowSetting["Reduce"]), name="addhtml")
    else:AddHtml = tk.Button(lfStep1, text="Add HTML file", command=CallAddHTML, state="disable", width=int(15 * WindowSetting["Reduce"]), name="addhtml")
    
    TextHtml = StringVar()
    TextHtml.set("Insert Path")
    CallEnableAddHtml = lambda event: EnableAddHtml(AddHtml, entryHtml.get())
    entryHtml = tk.Entry(lfStep1, textvariable=TextHtml, width=int(42 * WindowSetting["Reduce"]), name="entryhtml")
    entryHtml.bind("<Key>",CallEnableAddHtml)
    entryHtml.bind("<Return>",CallAddHTMLForEntry)

    CallOpenHTML = lambda: OpenHTML(lfStep1)
    if(platform.system() == 'Windows'):BrowseHtml = ttk.Button(lfStep1, text="Browse", command=CallOpenHTML, width=int(10 * WindowSetting["Reduce"]), name="browsehtml")
    else:BrowseHtml = tk.Button(lfStep1, text="Browse", command=CallOpenHTML, width=int(10 * WindowSetting["Reduce"]), name="browsehtml")


    CallReadFile = lambda: ReadFile(lfStep1, lfStep2, lfStep3, HtmlPath, WindowSetting, HtmlTable, ConversionDict, CardTable)
    if(platform.system() == 'Windows'):Read = ttk.Button(lfStep1, text="Read HTML file", command=CallReadFile, width=int(15 * WindowSetting["Reduce"]), name="read")
    else:Read = tk.Button(lfStep1, text="Read HTML file", command=CallReadFile, width=int(15 * WindowSetting["Reduce"]), name="read")
pass