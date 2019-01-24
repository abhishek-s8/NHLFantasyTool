def Overall_Time(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,AIT):
    AIT1 = IceTime2018(A1,A2) #Grab the average ice time data from previous 7 seasons
    AIT2 = IceTime2017(B1,B2)
    AIT3 = IceTime2016(C1,C2)
    AIT4 = IceTime2015(D1,D2)
    AIT5 = IceTime2014(E1,E2)
    AIT6 = IceTime2013(F1,F2)
    AIT7 = IceTime2012(G1,G2)
    
    ListOfStats = [AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7] #The List of Average Ice Time
    Total=0 #The total ice time added up to be able to average amount
    Division=0 #Number of times needed to be divided to average amount
    
    for num in ListOfStats: 
        if num != None: #If there are compareables from season
            Total = Total + num
            Division = Division + 1
            
    if Division > 0: #If there are any seasons that are compareable
        Average_Increment_Time = Total / Division
        
        if Average_Increment_Time < 0:
            Temporary = Average_Increment_Time * (-1) #For Division Purposes
        else:
            Temporary = Average_Increment_Time
            
        Minutes = Temporary // 60
        Seconds = (Temporary % 60)/100
        Minutes_Format = Minutes + Seconds 
        
        if Average_Increment_Time < 0: #To bring it back to negative if necessary
            Minutes_Format = Minutes_Format * (-1)
            
        Minutes_Format=round(Minutes_Format,2)
        Conversion_To_String = str(Minutes_Format)
        
        Position1 = AIT.find(":") #Find position to seperate minutes and second from data
        Position2 = Conversion_To_String.find(".") 
        
        Minutes = AIT[:Position1] #For The Player's Time
        Seconds = AIT[Position1+1:Position1+3]
        Minutes2 = Conversion_To_String[:Position2] #For the Increment Factor
        
        if Minutes2[:1]=="-": #For Division Purposes
            Minutes2=str(int(Minutes2)*(-1))
            
        Seconds2 = Conversion_To_String[Position2+1:]
        
        Seconds_From_Minutes1 = int(Minutes)*60
        Seconds_From_Minutes2 = int(Minutes2)*60
        
        Total_Seconds1 = Seconds_From_Minutes1 + int(Seconds)
        Total_Seconds2 = Seconds_From_Minutes2 + int(Seconds2)
        
        if Conversion_To_String[:1]=="-": #To bring it back to negative if necessar
            Total_Seconds2 = Total_Seconds2 * (-1)

        Estimated_Seconds = Total_Seconds1 + Total_Seconds2
        
        if Estimated_Seconds < 0: #If prediction goes to negative time it means they won't get time at all
            Estimated_Seconds = 0
            
        Final_Minutes = Estimated_Seconds // 60
        Final_Seconds = (Estimated_Seconds % 60)/100
        Final_Time = Final_Minutes + Final_Seconds 
        return Final_Time
    
    else: #In the scenario there wasn't any compareable players
        Position1 = AIT.find(":") #Find position to seperate minutes and second from data

        Minutes = AIT[:Position1] 
        Seconds = AIT[Position1+1:Position1+3]

        Seconds_From_Minutes1 = int(Minutes)*60

        Total_Seconds1 = Seconds_From_Minutes1 + int(Seconds)

        Final_Minutes = Total_Seconds1 // 60
        Final_Seconds = (Total_Seconds1 % 60)/100
        Final_Time = Final_Minutes + Final_Seconds 

        return Final_Time

def IceTime2018(A1,A2):
    Total=0 
    
    if len(A1)>0 and len(A2)>0: #If there were players for both seasons being compared
        for player in A1:
            count=0
            while count < len(A2): #Going through to find the same player
                if player[0] == A2[count][0]: #If same player grab time
                    Time1 = (player[16])
                    Time2 = (A2[count][16])
                    
                    Position1 = Time1.find(":") #Find position to seperate minutes and second from data
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1) #The player change in ice time
                    Total = Total + Difference #Add it to total to be averaged
                    count=len(A2)+1 #Do this to get out of loop
                else: #if you don't find same player keep going
                    count=count+1
                    
        Average_Increase_In_Time = Total / len(A1) #Now average it
    else:
        Average_Increase_In_Time = None #If there wasn't anyone to compare return nothing
    return Average_Increase_In_Time

def IceTime2017(B1,B2):
    Total=0
    
    if len(B1)>0 and len(B2)>0: #If there were players for both seasons being compared
        for player in B1:
            count=0
            while count < len(B2): #Going through to find the same player
                if player[0]==B2[count][0]: #If same player grab time
                    Time1 = (player[16])
                    Time2 = (B2[count][16])
                    
                    Position1 = Time1.find(":") #Find position to seperate minutes and second from data
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                    
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1) #The player change in ice time
                    Total = Total + Difference #Add it to total to be averaged
                    count=len(B2)+1 #Do this to get out of loop
                else: #if you don't find same player keep going
                    count=count+1
                    
        Average_Increase_In_Time=Total/len(B1) #Now average it
    else:
        Average_Increase_In_Time=None #If there wasn't anyone to compare return nothing
    return Average_Increase_In_Time

def IceTime2016(C1,C2):
    Total=0
    
    if len(C1)>0 and len(C2)>0:
        for player in C1:
            count=0
            while count < len(C2):
                if player[0]==C2[count][0]:
                    Time1 = (player[16])
                    Time2 = (C2[count][16])
                    
                    Position1 = Time1.find(":")
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(C2)+1  
                else:
                    count=count+1
                    
        Average_Increase_In_Time=Total/len(C1)
    else:
        Average_Increase_In_Time=None
    return Average_Increase_In_Time

def IceTime2015(D1,D2):
    Total=0
    
    if len(D1)>0 and len(D2)>0:
        for player in D1:
            count=0
            while count < len(D2):
                if player[0]==D2[count][0]:
                    Time1 = (player[16])
                    Time2 = (D2[count][16])
                    
                    Position1 = Time1.find(":")
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(D2)+1   
                else:
                    count=count+1
                    
        Average_Increase_In_Time=Total/len(D1)
    else:
        Average_Increase_In_Time=None
    return Average_Increase_In_Time

def IceTime2014(E1,E2):
    Total=0
    
    if len(E1)>0 and len(E2)>0:
        for player in E1:
            count=0
            while count < len(E2):
                if player[0]==E2[count][0]:
                    Time1 = (player[16])
                    Time2 = (E2[count][16])
                    
                    Position1 = Time1.find(":")
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(E2)+1
                else:
                    count=count+1
                    
        Average_Increase_In_Time=Total/len(E1)
    else:
        Average_Increase_In_Time=None
    return Average_Increase_In_Time

def IceTime2013(F1,F2):
    Total=0
    
    if len(F1)>0 and len(F2)>0:
        for player in F1:
            count=0
            while count < len(F2):
                if player[0]==F2[count][0]:
                    Time1 = (player[16])
                    Time2 = (F2[count][16])
                    
                    Position1 = Time1.find(":")
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(F2)+1
                else:
                    count=count+1
                    
        Average_Increase_In_Time=Total/len(F1)
    else:
        Average_Increase_In_Time=None
    return Average_Increase_In_Time

def IceTime2012(G1,G2):
    Total=0
    
    if len(G1)>0 and len(G2)>0:
        for player in G1:
            count=0
            while count < len(G2):
                if player[0]==G2[count][0]:
                    Time1 = (player[16])
                    Time2 = (G2[count][16])
                    
                    Position1 = Time1.find(":")
                    Position2 = Time2.find(":")
                    
                    Minutes1 = Time1[:Position1] 
                    Seconds1 = Time1[Position1+1:Position1+3]
                    Minutes2 = Time2[:Position2] 
                    Seconds2 = Time2[Position2+1:Position1+3]
                
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(G2)+1
                else:
                    count=count+1
                    
        Average_Increase_In_Time=Total/len(G1)
    else:
        Average_Increase_In_Time=None
    return Average_Increase_In_Time
