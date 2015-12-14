
def ReadHTML(HtmlPath, HtmlTable):
    for i in range(0, len(HtmlPath)):                        #Reads all the HTML files
        HtmlFile = open(HtmlPath[i], "r")
        Data = HtmlFile.read()
        HtmlFile.close
        Data = Data.replace('\n', '')
        Data = Data.replace('\t', '')
        Data = Data.replace("  ", " ")
        Data = Data.replace("   ", " ")
        Data = Data.replace("    ", "")
                     

        while(len(Data) > 0):                                #Current file treatment loop
            buffer = []
            
            if(Data[0] == 'p' and Data[1] == 'a' and Data[2] == 'n' and Data[3] == 'e' and Data[4] == 'l'):
                while(Data[0] != ' ' and Data[0] != '"'):
                    buffer.append(Data[0])
                    Data = Data[1:]
                if((''.join(buffer) in HtmlTable[0])==False):
                    HtmlTable[0].append(''.join(buffer))
            
            elif (Data[0] == 't' and Data[1] == 'h' and Data[2] == 'u' and Data[3] == 'm' and Data[4] == 'b' and Data[5] == 'n'and Data[6] == 'a'and Data[7] == 'i'and Data[8] == 'l'):
                while(Data[0] != ' ' and Data[0] != '"'):
                    buffer.append(Data[0])
                    Data = Data[1:]
                if((''.join(buffer) in HtmlTable[1])==False):
                    HtmlTable[1].append(''.join(buffer))
            
            elif(Data[0] == 'w' and Data[1] == 'e' and Data[2] == 'l' and Data[3] == 'l'):
                while(Data[0] != ' ' and Data[0] != '"'):
                    buffer.append(Data[0])
                    Data = Data[1:]
                if((''.join(buffer) in HtmlTable[2])==False):
                    HtmlTable[2].append(''.join(buffer))
            else:Data = Data[1:]

                
pass