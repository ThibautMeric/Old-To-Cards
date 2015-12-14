def RefreshStep3(lfStep3):

    lfStep3.children["generate"].grid(row=0, column=0, pady="10")
    lfStep3.grid_columnconfigure(0,minsize=525)
    lfStep3.grid_columnconfigure(1,minsize=525)
    lfStep3.children["reset"].grid(row=0, column=1, pady="10")
    lfStep3.grid(row=2, column=1, columnspan= 2,sticky="n s e w")

pass