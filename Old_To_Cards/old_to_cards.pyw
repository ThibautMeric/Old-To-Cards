# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Thibaut MERIC"
__date__ = "$4 dec. 2015 12:01:21$"

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
from Step1.InitializeStep1 import *
from Step2.InitializeStep2 import *
from Step3.InitializeStep3 import *
from Step1.RefreshStep1 import *
import os
import platform
import Old_To_Cards


    #######################
    ##GENERAL DECLARATION##
    #######################
Version = Old_To_Cards.__version__
HtmlPath = []
panel = []
thumbnail = []
whell = []
HtmlTable = [panel, thumbnail, whell]

PanelConversionDict = {
"panel": "card",
"panel-body": "card-text",
"panel-heading": "card-header",
"panel-title": "card-title",
"panel-footer": "card-footer",
"panel-group": "card-group",
#Color handeling below
"panel-default": "", # No default color in card system
"panel-primary": "card-primary",
"panel-success": "card-success",
"panel-info": "card-info",
"panel-warning": "card-warning",
"panel-danger": "card-danger"
}
ThumbnailConversionDict = {
"thumbnail": "card"
}
WellConversionDict = {
"well": "card",
"well-lg": "",
"well-sm": ""
}
ConversionDict = {"Panel":PanelConversionDict, "Thumbnail":ThumbnailConversionDict, "Well":WellConversionDict}
CardTable = [
" ",
"card",
"card-block",
"card-blockquote",
"card-columns",
"card-danger",
"card-deck",
"card-deck-wrapper",
"card-footer",
"card-group",
"card-header",
"card-img",
"card-img-overlay",
"card-img-top",
"card-img-bottom",
"card-info",
"card-inverse",
"card-link",
"card-primary",
"card-subtitle",
"card-success",
"card-text",
"card-title",
"card-warning",
]

    ##############################
    ##END OF GENERAL DECLARATION##
    ##############################
Window = Tk()
Window.resizable(width=False, height=False)
Window.title("Old to Cards " + Version)
WindowSetting = {}

if(platform.system() == 'Windows'):
    WindowSetting["Reduce"] = 1
    WindowSetting["Enlarge"] = 1
elif(platform.system() == 'Darwin'):
    WindowSetting["Reduce"] = 0.72
    WindowSetting["Enlarge"] = 1.1
else:
    WindowSetting["Reduce"] = 0.7
    WindowSetting["Enlarge"] = 1.2
    
lfStep1 = tk.LabelFrame(Window, text="Step1:")
lfStep2 = tk.LabelFrame(Window, text="Step2:")
lfStep3 = tk.LabelFrame(Window, text="Step3:")
    
InitializeStep1(lfStep1, lfStep2, lfStep3, WindowSetting, HtmlPath, Bottom, HtmlTable, ConversionDict, CardTable)
InitializeStep2(lfStep2)
InitializeStep3(lfStep1, lfStep2, lfStep3, WindowSetting, Version, HtmlPath, HtmlTable)
RefreshStep1(lfStep1, WindowSetting, HtmlPath)
Window.mainloop()