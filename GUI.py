from tkinter import*
import FrequencyFunctions as ff
import tkinter.messagebox

# Patrick Tumulty 
# Last Updated: Feb. 25 2019

root = Tk()
root.geometry("350x325")
root.title("TemperMental")

inputFrame = Frame(root)
freqList = Frame(root)

inputFrame.pack(side=TOP, padx=10, pady=10)
freqList.pack(side=TOP, padx=10, pady=10)

def addToList():
    majScale.delete(0, END)
    newScale.delete(0, END)
    centsOff.delete(0, END)
    frequency = float(numEntry.get())
    octDivider = int(OctaveDivider.get())
    ChromScale = ff.Create12TETChromatic(frequency)
    MajScale = ff.StandardMajScale(ChromScale)
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



freqLabel =     Label(inputFrame, text="Frequency:")
octLabel =      Label(inputFrame, text="Octave Divider:")
numEntry =      Entry(inputFrame)
OctaveDivider = Entry(inputFrame)
showButton =    Button(inputFrame, text="Show", command=addToList)

majScale = Listbox(freqList, width=10)
newScale = Listbox(freqList, width=10)
centsOff = Listbox(freqList, width=10)

# ---------------------- Buttons, Entry, and Lebel pack 

showButton.grid (row=0, columnspan=3)
freqLabel.grid  (row=1, column=0)
octLabel.grid   (row=2, column=0)
numEntry.grid   (row=1, column=1)
OctaveDivider.grid(row=2, column=1)

# ---------------------- Frequency Scales

majScale.pack(side=LEFT, padx=5)
newScale.pack(side=LEFT, padx=5)
centsOff.pack(side=LEFT, padx=5)


root.mainloop() 
