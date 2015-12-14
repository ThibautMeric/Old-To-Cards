def Replace(lfStep2, ClassName, HtmlText):
    TempText=""
    
    while(len(HtmlText)>0):
        if(ClassName==HtmlText[:len(ClassName)]):
            if((("-" in ClassName) and ("-" in HtmlText[:len(ClassName)])) or ((("-" in ClassName)==False) and (("-" in HtmlText[:len(ClassName)+1])==False))):
                try:
                    TempText += lfStep2.children["lfpanel"].children["new" + ClassName].get()
                except:
                    try:
                        TempText += lfStep2.children["lfthumbnail"].children["new" + ClassName].get()
                    except:
                        try:
                            TempText += lfStep2.children["lfwell"].children["new" + ClassName].get()
                        except:
                            print("error")

                HtmlText=HtmlText[len(ClassName):]
            else:
                TempText += HtmlText[:len(ClassName)]
                HtmlText=HtmlText[len(ClassName):]
        elif(ClassName[0] in HtmlText[:len(ClassName)]):
            TempText += HtmlText[:1]
            HtmlText=HtmlText[1:]
        else:
            TempText += HtmlText[:len(ClassName)]
            HtmlText=HtmlText[len(ClassName):]
               
    return (TempText)
pass