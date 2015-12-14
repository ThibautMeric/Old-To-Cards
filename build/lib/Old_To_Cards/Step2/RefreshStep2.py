try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
    
    
def RefreshStep2(lfStep2,HtmlTable, ConversionDict, CardTable):
    if (len(HtmlTable[0])==0):
        Label = tk.Label(lfStep2.children["lfpanel"], padx=60, pady=60,text= "No Panel in this HTML")
        Label.grid(row=1, column=1, sticky="n s e w")
    else:
        for i in range(0,len(HtmlTable[0])):
            Label = tk.Label(lfStep2.children["lfpanel"], text=HtmlTable[0][i], name =HtmlTable[0][i].lower())
            Arrow = tk.Label(lfStep2.children["lfpanel"], text="<--->")
            SelChoice = ttk.Combobox(lfStep2.children["lfpanel"], values=CardTable, state='readonly', name="new" + HtmlTable[0][i].lower())
            SelChoice.set(ConversionDict["Panel"][HtmlTable[0][i]])
            Label.grid(row=i, column=0,sticky="w")
            Arrow.grid(row=i, column=1,sticky="e w")
            SelChoice.grid(row=i, column=2,sticky="e")
    if (len(HtmlTable[1])==0):
        Label = tk.Label(lfStep2.children["lfthumbnail"], padx=60, pady=60, text= "No Thumbnail in this HTML")
        Label.grid(row=1, column=1, sticky="n s e w")
    else:
        for i in range(0,len(HtmlTable[1])):
            Label = tk.Label(lfStep2.children["lfthumbnail"], text=HtmlTable[1][i], name =HtmlTable[1][i].lower())
            Arrow = tk.Label(lfStep2.children["lfthumbnail"], text="<--->")
            SelChoice = ttk.Combobox(lfStep2.children["lfthumbnail"], values=CardTable, state='readonly', name="new" + HtmlTable[1][i].lower())
            SelChoice.set(ConversionDict["Thumbnail"][HtmlTable[1][i]])
            Label.grid(row=i, column=0,sticky="w")
            Arrow.grid(row=i, column=1,sticky="e w")
            SelChoice.grid(row=i, column=2,sticky="e")
    if (len(HtmlTable[2])==0):
        Label = tk.Label(lfStep2.children["lfwell"], padx=60, pady=60, text= "No Well in this HTML")
        Label.grid(row=1, column=1, sticky="n s e w")
    else:
        for i in range(0,len(HtmlTable[2])):
            Label = tk.Label(lfStep2.children["lfwell"], text=HtmlTable[2][i], name =HtmlTable[2][i].lower())
            Arrow = tk.Label(lfStep2.children["lfwell"], text="<--->")
            SelChoice = ttk.Combobox(lfStep2.children["lfwell"], values=CardTable, state='readonly', name="new" + HtmlTable[2][i].lower())
            SelChoice.set(ConversionDict["Well"][HtmlTable[2][i]])
            Label.grid(row=i, column=0,sticky="w")
            Arrow.grid(row=i, column=1,sticky="e w")
            SelChoice.grid(row=i, column=2,sticky="e")
            
    lfStep2.children["lfpanel"].grid(row=1, column=1, sticky="n s e w")
    lfStep2.children["lfthumbnail"].grid(row=1, column=2, sticky="n s e w")
    lfStep2.children["lfwell"].grid(row=1, column=3, sticky="n s e w")
    lfStep2.children["titlestep2"].grid(row=0, column=0, columnspan = 4, sticky="n s e w")
    lfStep2.grid(row=1, column=2, sticky="n s e w")
    
pass