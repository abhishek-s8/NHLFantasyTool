from tkinter import *
from collections import defaultdict
import bisect
import tkinter as tk
from tkinter import StringVar, Label, Button, font
from tkinter.ttk import Combobox
from string import ascii_uppercase
import math
import Data
import PowerTime as Time
import PowerPoints as PP
import Goals as G
import Assists as A
import OtherFactors as OF

class NHLFT_Gui(tk.Frame):
    NHLFT_S = list(Data.options.keys()) #The list of teams
    NHLFT_S.sort()
    Raw_Players=Data.options.get(NHLFT_S[0]) #For the first team get all the players

    Players = [] #Create a list of those players
    for part in Raw_Players:
        Players.append(part[0])
    Players.sort() #Sort player name for ease of use
    
    def __init__(self):
        '''Sets up the window and widgets'''
        tk.Frame.__init__(self)
        self.myfont = font.Font(family="Calibri", size=11, weight="normal")
        self.master.geometry("436x416")
        self.master.resizable(False, False)
        self.master.title("NHL Fantasy Tool 1.0")
        self.grid(sticky = 'NW')
        #Backgrounds and Images
        self.images()
        self.background()
        self.background2()
        self.background3()
        self.background4()
        self.logo()
        #Labels
        self.label()
        self.label2()
        self.label3()
        self.playerstats()
        self.predictions()
        self.guide()
        #The Buttons
        self.teambutton()
        self.playerbutton()
        self.conditions()
        self.combobox2()
        self.combobox()
        # Search Combobox values with keyboard
        self._Combo.bind("<Key>", self.findInBox)
        self._Combo2.bind("<Key>", self.findInBox2)
        self._Combo.focus()

    def images(self): 
        '''images method generate the background image'''
        self.image = tk.PhotoImage(file="Images/V1.png")
        self.header = tk.Label(self, image=self.image)
        self.header.place(x=0, y=0, relwidth=1, relheight=1)
        
    def logo(self):
        '''logo method generates the logo image'''
        self.image2 = tk.PhotoImage(file="Images/logo.png") #Place logo top right
        self.header2 = tk.Label(self, image=self.image2)
        self.header2.grid(row = 0, column = 3, pady=10, padx=10, rowspan=2)

    def guide(self): 
        '''guide method provides a guide for the user explaining the use'''
        Output="Guide"
        Output2="The NHL FT 1.0\npredicts a player's\nstats for the\n2018-2019 season\nby using previous\nhistory. This tool\nis intended for\nfantasy purposes.\nThis tool is NOT\nexactly accurate\nbut it is a FAIR\nestimate."
        self.guide1 = tk.Label(self, text = Output, font=self.myfont, bg='white', relief="raised", width=10)
        self.guide1.grid(row = 4, column = 2, columnspan=2)
        self.guide2 = tk.Label(self, text = Output2, font=self.myfont, bg='cornflower blue')
        self.guide2.grid(row = 5, column = 2, columnspan=2, rowspan=6)

    def background(self):
        '''background method generates the background for the previous season section'''
        self.canvas=tk.Canvas(self, background='lavender', highlightbackground="white") #Previous Season Background Background
        self.canvas.place(x=8, y=130, relwidth=0.28, relheight=0.60)

    def background2(self):
        '''background2 method generates the background for the prediction season section'''
        self.canvas=tk.Canvas(self, background='lavender', highlightbackground="white") #Prediction Background
        self.canvas.place(x=143, y=130, relwidth=0.33, relheight=0.60)

    def background3(self):
        '''background3 method generates the background for the guide section'''
        self.canvas=tk.Canvas(self, background='cornflower blue', highlightthickness=3, highlightbackground="white") #Guide Background
        self.canvas.place(x=304, y=130, relwidth=0.29, relheight=0.60)

    def background4(self):
        '''background4 method generates the background for the bottom bar'''
        self.canvas=tk.Canvas(self, background='Royal Blue', highlightthickness=0) 
        self.canvas.place(x=0, y=387, relwidth=1, relheight=0.06)

    def label(self):
        '''label method generates label for the selecting team'''
        self.Label = tk.Label(self, text = "Select Team:", font=self.myfont, relief=RIDGE,width=13, bg='gray')
        self.Label.grid(row = 0, column = 0, pady=10, padx=10, columnspan=1)

    def label2(self):
        '''label2 method generates label for the selecting player'''
        self.Label2 = tk.Label(self, text = "Select Player:", font=self.myfont, relief=RIDGE,width=13, bg='gray')
        self.Label2.grid(row = 1, column = 0, pady=10, padx=10, columnspan=1)

    def conditions(self):
        '''conditions method generates label for bottom bar'''
        self.condition = tk.Label(self, text = "1 - In All Situations   2 - During Power Play   3 - Assuming Healthy", font=self.myfont, bg='Royal Blue')
        self.condition.grid(row = 11, column = 0, pady=10, padx=10, columnspan=4)

    def combobox(self):
        '''combobox method generates box to select team'''
        self._ComboValue = tk.StringVar()
        self._Combo = Combobox(self, textvariable=self._ComboValue,
                                  state='readonly', height = '6',
                                  justify = 'center', font=self.myfont)
        self._Combo['values']= NHLFT_Gui.NHLFT_S # List of NHLFT s loaded into Combobox
        self._Combo.current(0) 
        self._Combo.grid(row = 0, column = 1, columnspan=1)

    def combobox2(self):
        '''combobox2 method generates box to select player'''
        self._ComboValue2 = tk.StringVar()
        self._Combo2 = Combobox(self, textvariable=self._ComboValue2,
                                  state='readonly', height = '6',
                                  justify = 'center', font=self.myfont)
        self._Combo2['values']= NHLFT_Gui.Players # List of NHLFT s loaded into Combobox
        self._Combo2.current(0)
        self._Combo2.grid(row = 1, column = 1, columnspan=1)
        
    def teambutton(self):
        self._button = tk.Button(self, text = "OK", font=self.myfont)
        self._button.bind('<Button-1>', self.ok)
        self._button.grid(row = 0, column = 2, padx=5, columnspan=1)

    def playerbutton(self):
        self._button = tk.Button(self, text = "OK", font=self.myfont)
        self._button.bind('<Button-1>', self.ok2)
        self._button.grid(row = 1, column = 2, padx=5, columnspan=1)
        
    def label3(self): #Acknowledge label when you select someone
        Output="You Selected: "
        self.Label3 = tk.Label(self, text = Output, font=self.myfont)
        self.Label3.grid(row = 3, column = 0, pady=10, columnspan=4)
    
    def playerstats(self): #Label that displays previous season stats when button is pressed
        Output="2017-2018 Season"
        Output1="Games : "
        Output2="Goals\u2081 : "
        Output3="Assists\u2081 : "
        Output4="Points\u2081 : "
        Output5="PP Goals\u2082 : "
        Output6="PP Assists\u2082 : "
        
        self.Label4 = tk.Label(self, text = Output, font=self.myfont, bg='lavender')
        self.Label4.grid(row = 4, column = 0, padx=10, columnspan=1)
        self.Label5 = tk.Label(self, text = Output1, font=self.myfont, bg='lavender')
        self.Label5.grid(row = 5, column = 0, pady=5, padx=10, columnspan=1)
        self.Label6 = tk.Label(self, text = Output2, font=self.myfont, bg='lavender')
        self.Label6.grid(row = 6, column = 0, pady=5, padx=10, columnspan=1)
        self.Label7 = tk.Label(self, text = Output3, font=self.myfont, bg='lavender')
        self.Label7.grid(row = 7, column = 0, pady=5, padx=10, columnspan=1)
        self.Label8 = tk.Label(self, text = Output4, font=self.myfont, bg='lavender')
        self.Label8.grid(row = 8, column = 0, pady=5, padx=10, columnspan=1)
        self.Label9 = tk.Label(self, text = Output5, font=self.myfont, bg='lavender')
        self.Label9.grid(row = 9, column = 0, pady=5, padx=10, columnspan=1)
        self.Label10 = tk.Label(self, text = Output6, font=self.myfont, bg='lavender')
        self.Label10.grid(row = 10, column = 0, pady=5, padx=10, columnspan=1)

    def predictions(self):
        Output="2018-2019 Prediction"
        Output1="Games\u2083 : "
        Output2="Goals\u2081 : "
        Output3="Assists\u2081 : "
        Output4="Points\u2081 : "
        Output5="PP Goals\u2082 : "
        Output6="PP Assists\u2082: "
        
        self.Label11 = tk.Label(self, text = Output, font=self.myfont, bg='lavender')
        self.Label11.grid(row = 4, column = 1, padx=10, columnspan=1)
        self.Label12 = tk.Label(self, text = Output1, font=self.myfont, bg='lavender')
        self.Label12.grid(row = 5, column = 1, pady=5, padx=10, columnspan=1)
        self.Label13 = tk.Label(self, text = Output2, font=self.myfont, bg='lavender')
        self.Label13.grid(row = 6, column = 1, pady=5, padx=10, columnspan=1)
        self.Label14 = tk.Label(self, text = Output3, font=self.myfont, bg='lavender')
        self.Label14.grid(row = 7, column = 1, pady=5, padx=10, columnspan=1)
        self.Label15 = tk.Label(self, text = Output4, font=self.myfont, bg='lavender')
        self.Label15.grid(row = 8, column = 1, pady=5, padx=10, columnspan=1)
        self.Label16 = tk.Label(self, text = Output5, font=self.myfont, bg='lavender')
        self.Label16.grid(row = 9, column = 1, pady=5, padx=10, columnspan=1)
        self.Label17 = tk.Label(self, text = Output6, font=self.myfont, bg='lavender')
        self.Label17.grid(row = 10, column = 1, pady=5, padx=10, columnspan=1)
    
    def ok2(self,event):
        '''ok2 method generate the estimated player production'''
        Raw_Players=Data.options.get(self._Combo.get())
        Players=[]
        
        for part in Raw_Players:
            Players.append(part[0])
            
        try:
            number=Players.index(self._Combo2.get())
        except(ValueError):
            self.Label3.config(text="You must press the first OK button")
            
        #The various statistics
        selected=Raw_Players[number]
        Age=selected[1]
        Position=selected[2]
        PPG=selected[3]
        GPG=selected[4]
        APG=selected[5]
        Corsi=selected[11]
        PDO=selected[12]
        OZone=selected[13]
        AverageIceTime=selected[15]
        PPTime=selected[17]
        Games=selected[18]
        Goals=selected[19]
        PPGoals=selected[21]
        Assists=selected[22]
        PPAssists=selected[24]
        PowerPlayGame=selected[25]
        PowerPlayAGame=selected[26]
        Points=selected[27]
        
        self.Label3.config(text="You Selected: "+self._Combo2.get())
        self.Label5.config(text="Games : "+Games)
        self.Label6.config(text="Goals\u2081 : "+Goals)
        self.Label7.config(text="Assists\u2081 : "+Assists)
        self.Label8.config(text="Points\u2081 : "+Points)
        self.Label9.config(text="PP Goals\u2082 : "+PPGoals)
        self.Label10.config(text="PP Assists\u2082 : "+PPAssists)

        Entry=Data.points2(Age) #Finds the refer point for ages in 2017
        entry1=Entry[0] #Starting Point
        entry2=Entry[1] #Ending Point
        people=Data.collect2017(entry1,entry2,PPG,Position) #The people in that PPG range 2017

        Entry=Data.points3(Age) #Finds the refer point for ages in 2016
        entry1=Entry[0] 
        entry2=Entry[1] 
        people2=Data.collect2016(entry1,entry2,PPG,Position) #The people in that PPG range 2016

        Entry=Data.points4(Age) #Finds the refer point for ages in 2015
        entry1=Entry[0] 
        entry2=Entry[1] 
        people3=Data.collect2015(entry1,entry2,PPG,Position) #The people in that PPG range 2015

        Entry=Data.points5(Age) #Finds the refer point for ages in 2015
        entry1=Entry[0] 
        entry2=Entry[1] 
        people4=Data.collect2014(entry1,entry2,PPG,Position) #The people in that PPG range 2014

        Entry=Data.points6(Age) #Finds the refer point for ages in 2015
        entry1=Entry[0] 
        entry2=Entry[1] 
        people5=Data.collect2013(entry1,entry2,PPG,Position) #The people in that PPG range 2013

        Entry=Data.points7(Age) #Finds the refer point for ages in 2015
        entry1=Entry[0] 
        entry2=Entry[1] 
        people6=Data.collect2012(entry1,entry2,PPG,Position) #The people in that PPG range 2012

        Entry=Data.points8(Age) #Finds the refer point for ages in 2015
        entry1=Entry[0] 
        entry2=Entry[1] 
        people7=Data.collect2011(entry1,entry2,PPG,Position) #The people in that PPG range 2011

        Updated_Age=int(Age)+1 #Seeing their next year age for next year results
        
        Entry=Data.points(str(Updated_Age)) #Finding points with updated age in 2018
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup=Data.compare2018(entry1,entry2,people) #Those Players' Stats the Next Year

        Entry=Data.points2(str(Updated_Age)) #Finding points with updated age in 2017
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup2=Data.compare2017(entry1,entry2,people2) #Those Players' Stats the Next Year

        Entry=Data.points3(str(Updated_Age)) #Finding points with updated age in 2016
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup3=Data.compare2016(entry1,entry2,people3) #Those Players' Stats the Next Year

        Entry=Data.points4(str(Updated_Age)) #Finding points with updated age in 2015
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup4=Data.compare2015(entry1,entry2,people4) #Those Players' Stats the Next Year

        Entry=Data.points5(str(Updated_Age)) #Finding points with updated age in 2014
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup5=Data.compare2014(entry1,entry2,people5) #Those Players' Stats the Next Year

        Entry=Data.points6(str(Updated_Age)) #Finding points with updated age in 2013
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup6=Data.compare2013(entry1,entry2,people6) #Those Players' Stats the Next Year

        Entry=Data.points7(str(Updated_Age)) #Finding points with updated age in 2012
        entry1=Entry[0] 
        entry2=Entry[1] 
        nextup7=Data.compare2012(entry1,entry2,people7) #Those Players' Stats the Next Year

        PPG=PP.PowerplayGoals(people,nextup,people2,nextup2,people3,nextup3,
                              people4,nextup4,people5,nextup5,people6,nextup6,
                              people7,nextup7,PPTime,PowerPlayGame)
        
        PPA=PP.PowerplayAssists(people,nextup,people2,nextup2,people3,nextup3,
                                people4,nextup4,people5,nextup5,people6,nextup6,
                                people7,nextup7,PPTime,PowerPlayAGame)
        
        GOALS=G.TotalGoals(people,nextup,people2,nextup2,people3,nextup3,
                           people4,nextup4,people5,nextup5,people6,nextup6,
                           people7,nextup7,AverageIceTime,GPG,Age)
        
        ASSISTS=A.TotalAssists(people,nextup,people2,nextup2,people3,nextup3,
                               people4,nextup4,people5,nextup5,people6,nextup6,
                               people7,nextup7,AverageIceTime,APG,Age)
        
        ADJUSTMENT=OF.FinalAdjustment(people,people2,people3,people4,people5,people6,people7
                                        ,Corsi,PDO,OZone,GOALS,ASSISTS)
        
        GOALS=ADJUSTMENT[0] #Grab final results
        ASSISTS=ADJUSTMENT[1]
        
        self.Label12.config(text="Games\u2083 : 82")
        self.Label13.config(text="Goals\u2081 : "+str(round(GOALS)))
        self.Label14.config(text="Assists\u2081 : "+str(round(ASSISTS)))
        self.Label15.config(text="Points\u2081 : "+str(round(ASSISTS+GOALS)))
        self.Label16.config(text="PP Goals\u2082 : "+str(round(PPG)))
        self.Label17.config(text="PP Assists\u2082 : "+str(round(PPA)))

    def ok(self, event): #When user clicks first ok button
        '''ok method allows the user to generate a list value of the team players'''
        Raw_Players=Data.options.get(self._Combo.get())
        Players=[]
        for part in Raw_Players:
            Players.append(part[0])
        Players.sort()
        self._Combo2['values']= Players
        self._Combo2.current(0)
            
    def findInBox(self, event):
        '''findInBox method allows the user to search through the list values by keyboard press'''
        keypress = event.char.upper()
        if keypress in ascii_uppercase: # If user key press is in the alphabet
            for index, _name in enumerate(NHLFT_Gui.NHLFT_S):
                if _name.startswith(keypress):
                    self._Combo.current(index)
                    break
                
    def findInBox2(self, event):
        '''findInBox2 allows the user to search through the list values by keyboard press'''
        keypress = event.char.upper()
        if keypress in ascii_uppercase: # If user key press is in the alphabet
            for index, _name in enumerate(NHLFT_Gui.Players):
                if _name.startswith(keypress):
                    self._Combo2.current(index)
                    break
    
def main():
    NHLFT_Gui().mainloop()

main()


    
