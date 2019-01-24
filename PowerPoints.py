import PowerTime as Time

def PowerplayGoals(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPT,PPG):
    Powerplay_Time=Time.Overall_PP_Time(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPT) #The Player's Predicted Power Play Time a Game
    Powerplay_Goals=PowerplayGoalsProcess(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPG) #The Player's Predicted Power Play Goals a Game

    if Powerplay_Time != 0:
        PowerPG =(Powerplay_Goals/Powerplay_Time)*(82*Powerplay_Time)
    else:
        PowerPG=0
    return PowerPG

def PowerplayAssists(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPT,PPA):
    Powerplay_Time=Time.Overall_PP_Time(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPT) #The Player's Predicted Power Play Time a Game
    Powerplay_Assists=PowerplayAssistsProcess(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPA) #The Player's Predicted Power Play Goals a Game

    if Powerplay_Time != 0:
        PowerPA =(Powerplay_Assists/Powerplay_Time)*(82*Powerplay_Time)
    else:
        PowerPA=0
    return PowerPA

def PowerplayAssistsProcess(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPA):
    PP1=AVG_PP_Assists2018(A1,A2)
    PP2=AVG_PP_Assists2017(B1,B2)
    PP3=AVG_PP_Assists2016(C1,C2)
    PP4=AVG_PP_Assists2015(D1,D2)
    PP5=AVG_PP_Assists2014(E1,E2)
    PP6=AVG_PP_Assists2013(F1,F2)
    PP7=AVG_PP_Assists2012(G1,G2)

    ListOfStats = [PP1,PP2,PP3,PP4,PP5,PP6,PP7]
    Total=0
    Division=0

    for num in ListOfStats:
        if num != None:
            Total = Total + num
            Division = Division + 1

    if Division > 0:
        PP_Assists_Factor = Total / Division
        New_Prediction = float(PPA) + PP_Assists_Factor
        if New_Prediction<0:
            New_Prediction=PPA
        return float(New_Prediction)
    else:
        return float(PPA) 
    
def PowerplayGoalsProcess(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,PPG):
    PP1=AVG_PP_Goals2018(A1,A2)
    PP2=AVG_PP_Goals2017(B1,B2)
    PP3=AVG_PP_Goals2016(C1,C2)
    PP4=AVG_PP_Goals2015(D1,D2)
    PP5=AVG_PP_Goals2014(E1,E2)
    PP6=AVG_PP_Goals2013(F1,F2)
    PP7=AVG_PP_Goals2012(G1,G2)

    ListOfStats = [PP1,PP2,PP3,PP4,PP5,PP6,PP7]
    Total=0
    Division=0

    for num in ListOfStats:
        if num != None:
            Total = Total + num
            Division = Division + 1
    if Division > 0:
        PP_Goals_Factor = Total / Division
        New_Prediction = float(PPG) + PP_Goals_Factor
        if New_Prediction<0:
            New_Prediction=PPG
        return float(New_Prediction)
    else:
        return float(PPG)

def AVG_PP_Goals2018(A1,A2):
    Total=0
    if len(A1)>0 and len(A2)>0:
        for player in A1:
            count=0
            while count < len(A2):
                if player[0]==A2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (A2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(A2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(A1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Goals2017(B1,B2):
    Total=0
    if len(B1)>0 and len(B2)>0:
        for player in B1:
            count=0
            while count < len(B2):
                if player[0]==B2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (B2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(B2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(B1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Goals2016(C1,C2):
    Total=0
    if len(C1)>0 and len(C2)>0:
        for player in C1:
            count=0
            while count < len(C2):
                if player[0]==C2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (C2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(C2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(C1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Goals2015(D1,D2):
    Total=0
    if len(D1)>0 and len(D2)>0:
        for player in D1:
            count=0
            while count < len(D2):
                if player[0]==D2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (D2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(D2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(D1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Goals2014(E1,E2):
    Total=0
    if len(E1)>0 and len(E2)>0:
        for player in E1:
            count=0
            while count < len(E2):
                if player[0]==E2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (E2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(E2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(E1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Goals2013(F1,F2):
    Total=0
    if len(F1)>0 and len(F2)>0:
        for player in F1:
            count=0
            while count < len(F2):
                if player[0]==F2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (F2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(F2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(F1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Goals2012(G1,G2):
    Total=0
    if len(G1)>0 and len(G2)>0:
        for player in G1:
            count=0
            while count < len(G2):
                if player[0]==G2[count][0]:
                    Avg_PPG1 = (player[26])
                    Avg_PPG2 = (G2[count][26])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(G2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(G1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2018(A1,A2):
    Total=0
    if len(A1)>0 and len(A2)>0:
        for player in A1:
            count=0
            while count < len(A2):
                if player[0]==A2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (A2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(A2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(A1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2017(B1,B2):
    Total=0
    if len(B1)>0 and len(B2)>0:
        for player in B1:
            count=0
            while count < len(B2):
                if player[0]==B2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (B2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(B2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(B1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2016(C1,C2):
    Total=0
    if len(C1)>0 and len(C2)>0:
        for player in C1:
            count=0
            while count < len(C2):
                if player[0]==C2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (C2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(C2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(C1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2015(D1,D2):
    Total=0
    if len(D1)>0 and len(D2)>0:
        for player in D1:
            count=0
            while count < len(D2):
                if player[0]==D2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (D2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(D2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(D1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2014(E1,E2):
    Total=0
    if len(E1)>0 and len(E2)>0:
        for player in E1:
            count=0
            while count < len(E2):
                if player[0]==E2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (E2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(E2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(E1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2013(F1,F2):
    Total=0
    if len(F1)>0 and len(F2)>0:
        for player in F1:
            count=0
            while count < len(F2):
                if player[0]==F2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (F2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(F2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(F1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG

def AVG_PP_Assists2012(G1,G2):
    Total=0
    if len(G1)>0 and len(G2)>0:
        for player in G1:
            count=0
            while count < len(G2):
                if player[0]==G2[count][0]:
                    Avg_PPG1 = (player[27])
                    Avg_PPG2 = (G2[count][27])
                    Difference = float(Avg_PPG2) - float(Avg_PPG1)
                    Total = Total + Difference
                    count=len(G2)+1
                else:
                    count=count+1
        Increase_In_PPG=Total/len(G1)
    else:
        Increase_In_PPG=None
    return Increase_In_PPG
