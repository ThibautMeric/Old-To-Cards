try:
    from tkinter.filedialog import *
    import tkinter.messagebox
except:
    from tkFileDialog import *
    import tkMessageBox
import platform
import os
from Others.Replace import*


def Generate(HtmlPath, HtmlTable, lfStep2):
    
    for i in range(0,len(HtmlPath)):
        if(os.path.isfile(str(HtmlPath[i])) == False):
            try:
                tkinter.messagebox.showerror ("Error: HTML not available", HtmlPath[i][-40:] + "is not available anymore.")
            except:
                tkMessageBox.showerror ("Error: HTML not available", HtmlPath[i][-40:] + "is not available anymore.")
            return
    
    for i in range(0,len(HtmlPath)):
        HtmlFile = open(HtmlPath[i], "r")
        Data = HtmlFile.read()
        DataNew = "<!-- Updated with Microchip-Old-To-Cards-->\n"
        HtmlFile.close
        Flag= True
        index=0
        for i in range(0,len(HtmlTable)):
            for y in range(0,len(HtmlTable[i])):
                Data = Replace(lfStep2,HtmlTable[i][y],Data)    
        
        SaveAs = asksaveasfile(mode='w', defaultextension="",title="Save As:", filetypes=[('HTML files', '.html')])
        if SaveAs is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        name= SaveAs.name
        if SaveAs.name[(len(SaveAs.name)-5):]!=".html":
            os.rename(SaveAs.name,SaveAs.name +".html")
            name+=".html"
        SaveAs.write("<!--Converted with Old to Cards -->\n" + Data)
        SaveAs.close()
        try:
            tkinter.messagebox.showinfo("Conversion, successful","Your file was successfully generated under:\n"+name)
        except:
            tkMessageBox.showinfo("Conversion, successful","Your file was successfully generated under:\n"+name)
                
pass