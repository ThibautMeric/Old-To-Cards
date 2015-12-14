from Step1.RefreshStep1 import *

def Reset(lfStep1, lfStep2, lfStep3, HtmlPath, HtmlTable, WindowSetting):

    # re enable path modifications
    try:
        lfStep1.children["browsehtml"].configure(state="active")
        lfStep1.children["read"].configure(state="active")
        lfStep1.children["entryhtml"].configure(state="active")
    except:
        lfStep1.children["browsehtml"].configure(state="normal")
        lfStep1.children["read"].configure(state="normal")
        lfStep1.children["entryhtml"].configure(state="normal")

    # Reset display

    lfStep2.grid_forget()
    lfStep3.grid_forget()

    for i in lfStep2.children["lfpanel"].winfo_children():
        i.destroy()
        
    for i in lfStep2.children["lfthumbnail"].winfo_children():
        i.destroy()
        
    for i in lfStep2.children["lfwell"].winfo_children():
        i.destroy()
    
    #Reset data
    
    for i in range(0, len(HtmlPath)):
        del HtmlPath[0]
    for i in range(0, len(HtmlTable)):
        for y in range(0, len(HtmlTable[i])):
            del HtmlTable[i][0]

    #Refresh

    RefreshStep1(lfStep1,WindowSetting, HtmlPath)

pass