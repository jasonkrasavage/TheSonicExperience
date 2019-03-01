from tkinter import*
import FrequencyFunctions as ff
import tkinter.messagebox

# Patrick Tumulty 
# Last Updated: Feb. 28 2019

# ---------- instantiate our window ------------------

#root = Tk()
root.title("TemperMental")
root.resizable(width=False, height=False)

# ---------- window frames ----------------------------

inputFrame = Frame(root)
freqList = Frame(root)
chordButtons = Frame(root)
sendOptions = Frame(root)

# ---------- window frame .pack ------------------------

inputFrame.pack(side=TOP, padx=10, pady=10)
freqList.pack(side=TOP, padx=10, pady=10)
chordButtons.pack(side=TOP, padx=10, pady=10)
sendOptions.pack(side=TOP, padx=10, pady=10)

# ---------- gui variables ------------------------------

variable = StringVar()
v = IntVar()

# ---------- gui functions ------------------------------

def change_state(*args):
    """Updates the state of the program once a scale has been selected"""
    scale = variable.get()
    if scale == "TET":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=NORMAL)
        status.config(text="create a new equal tempered scale...")
    elif scale == "Just":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        status.config(text="create a just scale...")
    elif scale == "Pythagorean":
        showButton.config(state=NORMAL)
        OctaveDivider.config(state=DISABLED)
        status.config(text="create a pythagorean scale...")

variable.trace('w', change_state) #checks to see which option has been selected

def addToList():
    majScale.delete(0, END)
    newScale.delete(0, END)
    centsOff.delete(0, END)
    if variable.get() == "TET":
        frequency = float(numEntry.get())
        octDivider = int(OctaveDivider.get())
        status.config(text="Major Scale / New TET Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        newTET = ff.TETMajScale(frequency, octDivider) 
        cents = ff.calculateCents(MajScale, newTET)
        for i in range(len(MajScale)):
            val = MajScale[i]
            majScale.insert(END, val)
        for i in range(len(newTET)):
            val = newTET[i]
            newScale.insert(END, val)
        for i in range(len(cents)):
            val = cents[i]
            centsOff.insert(END, int(val))
    elif variable.get() == "Just":
        frequency = float(numEntry.get())
        status.config(text="Major Scale / Just Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        Just = ff.JustScale(frequency)
        cents = ff.calculateCents(MajScale, Just)
        for i in range(len(MajScale)):
            val = MajScale[i]
            majScale.insert(END, val)
        for i in range(len(Just)):
            val = Just[i]
            newScale.insert(END, val)
        for i in range(len(cents)):
            val = cents[i]
            centsOff.insert(END, int(val))
    elif variable.get() == "Pythagorean":
        frequency = float(numEntry.get())
        status.config(text="Major Scale / Pythagorean Scale / Cents Off...")
        MajScale = ff.StandardMajScale(frequency)
        Pyth = ff.PythagoreanScale(frequency)
        cents = ff.calculateCents(MajScale, Pyth)
        for i in range(len(MajScale)):
            val = MajScale[i]
            majScale.insert(END, val)
        for i in range(len(Pyth)):
            val = Pyth[i]
            newScale.insert(END, val)
        for i in range(len(cents)):
            val = cents[i]
            centsOff.insert(END, int(val))
        
# --------- Tkinter Widgets ---------------------------

ScaleOption =   OptionMenu(inputFrame, variable, "TET", "Just", "Pythagorean")
freqLabel =     Label(inputFrame, text="Frequency:")
scaleLabel =    Label(inputFrame, text="Choose Scale:")
numEntry =      Entry(inputFrame, width=10)
OctaveDivider = Entry(inputFrame, width=10, state=DISABLED)
showButton =    Button(inputFrame, text="Show", command=addToList, state=DISABLED)
status = Label(root, text="Welcome!", bd=1, relief=SUNKEN, anchor=W)

one =   Button(chordButtons, text="I", width=8, height=3).grid(row=0, column=0)
two =   Button(chordButtons, text="II", width=8, height=3).grid(row=0, column=1)
three = Button(chordButtons, text="III", width=8, height=3).grid(row=0, column=2)
four =  Button(chordButtons, text="IV", width=8, height=3).grid(row=0, column=3)
five =  Button(chordButtons, text="V", width=8, height=3).grid(row=1, column=0)
six =   Button(chordButtons, text="VI", width=8, height=3).grid(row=1, column=1)
seven = Button(chordButtons, text="VII", width=8, height=3).grid(row=1, column=2)
eight = Button(chordButtons, text="VIII", width=8, height=3).grid(row=1, column=3)

soloMajor = Radiobutton(sendOptions, text="12 TET", variable=v, value=1).pack(side=LEFT)
soloNew = Radiobutton(sendOptions, text="New Scale", variable=v, value=2).pack(side=LEFT)
Both = Radiobutton(sendOptions, text="Both", variable=v, value=3).pack(side=LEFT)

majScale = Listbox(freqList, width=10)
newScale = Listbox(freqList, width=10)
centsOff = Listbox(freqList, width=10)

# ---------------------- Buttons, Entry, and Label pack ------------

showButton.grid (row=0, columnspan=3)
freqLabel.grid(row=1, column=0)
scaleLabel.grid(row=2, column=0)
numEntry.grid(row=1, column=1)
OctaveDivider.grid(row=3, column=1)
ScaleOption.grid(row=2, column=1)
status.pack(side=BOTTOM, fill=X)

# ---------------------- Frequency Scales --------------

majScale.pack(side=LEFT, padx=5)
newScale.pack(side=LEFT, padx=5)
centsOff.pack(side=LEFT, padx=5)


root.mainloop() 
