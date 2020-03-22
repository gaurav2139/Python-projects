from tkinter import *

def calc_body(source, side):
    body = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    body.pack(side=side, expand =YES, fill =BOTH)
    return body

def button(source, side, text, command=None):
    body = Button(source, text=text, command=command)
    body.pack(side=side, expand = YES, fill=BOTH)
    return body

class calc(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font", "arial 32")
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')

        screen =StringVar()
        Entry(self, bg = 'light blue', bd = 20, relief = SUNKEN, textvariable=screen, justify = RIGHT).pack(side = TOP, expand = YES, fill=BOTH)
        for CB in (["C"]):
            erase = calc_body(self, TOP)
            for ichar in CB:
                button(erase, LEFT, ichar, lambda body= screen, q=ichar: body.set(''))

        for NB in ("789/", "456*", "123-", "0.+"):
         FunctionNum = calc_body(self, TOP)
         for iEquals in NB:
            button(FunctionNum, LEFT, iEquals, lambda body=screen, q=iEquals: body.set(body.get() + q))

        EB = calc_body(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EB, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self, body=screen: s.calc(body), '+')

            else:
                btniEquals = button(EB, LEFT, iEquals, lambda body=screen, s=' %s ' % iEquals: body.set(body.get() + s))

    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")

if __name__=='__main__':
    calc().mainloop()