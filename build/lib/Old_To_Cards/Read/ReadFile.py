from Old_To_Cards.Read.ReadHtml import *
from Old_To_Cards.Step1.RefreshStep1 import *
from Old_To_Cards.Step2.RefreshStep2 import *
from Old_To_Cards.Step3.RefreshStep3 import *
import os

def ReadFile(lfStep1, lfStep2, lfStep3, HtmlPath, WindowSetting, HtmlTable, ConversionDict, CardTable):

    #Unexpected action handler


    if(len(HtmlPath) == 0):
        try:
            tkinter.messagebox.showerror ("Error: No HTML", "Please add an HTML file")
        except:
            tkMessageBox.showerror ("Error: No HTML", "Please add an HTML file")
        return
    else:

        Error = "The following files are unvalid:"
        DefaultErrorLenght = len(Error)
        RemoveHtml = []

        for i in range(0, len(HtmlPath)):
            if(os.path.isfile(str(HtmlPath[i])) == False):
                Error += "\n..." + HtmlPath[i][-40:] + ": Not Found" + "\n"
                RemoveHtml.append(i)
        for i in RemoveHtml[::-1]:
            HtmlPath.remove(HtmlPath[i])
        RemoveHtml = []

        for i in range(0, len(HtmlPath)):
            if(HtmlPath[i][-5] != "." or HtmlPath[i][-4] != "h" or HtmlPath[i][-3] != "t" or HtmlPath[i][-2] != "m" or HtmlPath[i][-1] != "l"):
                Error += "\n..." + HtmlPath[i][-40:] + ": Not HTML" + "\n"
                RemoveHtml.append(i)
        for i in RemoveHtml[::-1]:
            HtmlPath.remove(HtmlPath[i])
        RemoveHtml = []

        for i in range(0, len(HtmlPath)):
            if(HtmlPath.count(HtmlPath[i]) > 1):
                Error += "\n..." + HtmlPath[i][-40:] + ": Found Multiple times" + "\n"
                RemoveHtml.append(i)

        for i in RemoveHtml[::-1]:
            del HtmlPath[i]
        RemoveHtml = []

        if(len(Error) > DefaultErrorLenght):
            try:
                tkinter.messagebox.showerror ("Error: Incorrect File(s)", Error)
            except:
                tkMessageBox.showerror ("Error: Incorrect File(s)", Error)
            RefreshStep1(lfStep1,WindowSetting, HtmlPath)
            lfStep1.children["read"].grid(row= len(HtmlPath) + 3, column=0, pady="5")
            return


    # Disable path modifications

    lfStep1.children["browsehtml"].configure(state="disabled")
    lfStep1.children["read"].configure(state="disabled")
    lfStep1.children["entryhtml"].configure(state="disabled")

    #Read the files

    ReadHTML(HtmlPath, HtmlTable)

    #Display Step 2

    RefreshStep2(lfStep2,HtmlTable, ConversionDict, CardTable)

    #Display Step 3

    RefreshStep3(lfStep3)

pass
