def Overall_PP_Time(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPT):
    PP1=AVG_PP_Time2018(A1,A2) #The seconds increase / decrease of time
    PP2=AVG_PP_Time2017(B1,B2)
    PP3=AVG_PP_Time2016(C1,C2)
    PP4=AVG_PP_Time2015(D1,D2)
    PP5=AVG_PP_Time2014(E1,E2)
    PP6=AVG_PP_Time2013(F1,F2)
    PP7=AVG_PP_Time2012(G1,G2)

    ListOfStats = [PP1,PP2,PP3,PP4,PP5,PP6,PP7]
    Total=0
    Division=0

    for num in ListOfStats:
        if num != None:
            Total = Total + num
            Division = Division + 1

    if Division > 0:
        Average_PP_Increment_Time = Total / Division

        if Average_PP_Increment_Time < 0:
            Temporary = Average_PP_Increment_Time * (-1)#For Division Purposes
        else:
            Temporary = Average_PP_Increment_Time

        Minutes = Temporary // 60
        Seconds = (Temporary % 60)/100
        Minutes_Format = Minutes + Seconds

        if Average_PP_Increment_Time < 0:
            Minutes_Format = Minutes_Format * (-1)

        Minutes_Format=round(Minutes_Format,2)
        Conversion_To_String = str(Minutes_Format)
        
        Position1 = PPT.find(":") 
        Position2 = Conversion_To_String.find(".")
        
        Minutes = PPT[:Position1] #For The Player's Time
        Seconds = PPT[Position1+1:]

        Minutes2 = Conversion_To_String[:Position2] #For the Increment Factor

        if Minutes2[:1]=="-":
            Minutes2=str(int(Minutes2)*(-1))

        Seconds2 = Conversion_To_String[Position2+1:]

        Seconds_From_Minutes1 = int(Minutes)*60
        Seconds_From_Minutes2 = int(Minutes2)*60
        
        Total_Seconds1 = Seconds_From_Minutes1 + int(Seconds)
        Total_Seconds2 = Seconds_From_Minutes2 + int(Seconds2)

        if Conversion_To_String[:1]=="-":
            Total_Seconds2 = Total_Seconds2 * (-1)

        Estimated_PP_Seconds = Total_Seconds1 + Total_Seconds2

        if Estimated_PP_Seconds < 0:
            Estimated_PP_Seconds = 0

        Final_Minutes = Estimated_PP_Seconds // 60
        Final_Seconds = (Estimated_PP_Seconds % 60)/100
        Final_Time = Final_Minutes + Final_Seconds
        return Final_Time
    else:
        Position1 = PPT.find(":")

        Minutes = PPT[:Position1] 
        Seconds = PPT[Position1+1:]

        Seconds_From_Minutes1 = int(Minutes)*60
        Total_Seconds1 = Seconds_From_Minutes1 + int(Seconds)

        Final_Minutes = Total_Seconds1 // 60
        Final_Seconds = (Total_Seconds1 % 60)/100
        Final_Time = Final_Minutes + Final_Seconds
        return Final_Time
        
def AVG_PP_Time2018(A1,A2):
    Total=0
    if len(A1)>0 and len(A2)>0:
        for player in A1:
            count=0
            while count < len(A2):
                if player[0]==A2[count][0]:
                    Time1 = (player[18])
                    Time2 = (A2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                    
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(A2)+1
                else:
                    count=count+1
        Average_Increase_In_Time = Total / len(A1)
    else:
        Average_Increase_In_Time = None
    return Average_Increase_In_Time

def AVG_PP_Time2017(B1,B2):
    Total=0
    if len(B1)>0 and len(B2)>0:
        for player in B1:
            count=0
            while count < len(B2):
                if player[0]==B2[count][0]:
                    Time1 = (player[18])
                    Time2 = (B2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                    
                    Seconds_From_Minutes1 = int(Minutes1)*60
                    Seconds_From_Minutes2 = int(Minutes2)*60

                    Total_Time1 = Seconds_From_Minutes1 + int(Seconds1)
                    Total_Time2 = Seconds_From_Minutes2 + int(Seconds2)
                    
                    Difference = float(Total_Time2)-float(Total_Time1)
                    Total = Total + Difference
                    count=len(B2)+1
                else:
                    count=count+1
        Average_Increase_In_Time=Total/len(B1)
    else:
        Average_Increase_In_Time=None
    return Average_Increase_In_Time

def AVG_PP_Time2016(C1,C2):
    Total=0
    if len(C1)>0 and len(C2)>0:
        for player in C1:
            count=0
            while count < len(C2):
                if player[0]==C2[count][0]:
                    Time1 = (player[18])
                    Time2 = (C2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                
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

def AVG_PP_Time2015(D1,D2):
    Total=0
    if len(D1)>0 and len(D2)>0:
        for player in D1:
            count=0
            while count < len(D2):
                if player[0]==D2[count][0]:
                    Time1 = (player[18])
                    Time2 = (D2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                
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

def AVG_PP_Time2014(E1,E2):
    Total=0
    if len(E1)>0 and len(E2)>0:
        for player in E1:
            count=0
            while count < len(E2):
                if player[0]==E2[count][0]:
                    Time1 = (player[18])
                    Time2 = (E2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                
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

def AVG_PP_Time2013(F1,F2):
    Total=0
    if len(F1)>0 and len(F2)>0:
        for player in F1:
            count=0
            while count < len(F2):
                if player[0]==F2[count][0]:
                    Time1 = (player[18])
                    Time2 = (F2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                
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

def AVG_PP_Time2012(G1,G2):
    Total=0
    if len(G1)>0 and len(G2)>0:
        for player in G1:
            count=0
            while count < len(G2):
                if player[0]==G2[count][0]:
                    Time1 = (player[18])
                    Time2 = (G2[count][18])
                    
                    Minutes1 = Time1[:1] 
                    Seconds1 = Time1[2:]
                    Minutes2 = Time2[:1] 
                    Seconds2 = Time2[2:]
                
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

