import AllTime as Time

def TotalGoals(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,AIT,GPG,Age):
    Goals_Per_Game = GoalsProcess(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,GPG,Age)
    Time_Per_Game=Time.Overall_Time(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,AIT)
    Total_Goals=(Goals_Per_Game / Time_Per_Game)*(Time_Per_Game * 82)
    return Total_Goals
    
def GoalsProcess(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,GPG,Age):
    GPG1 = Goals_Per_Game2018(A1,A2)
    GPG2 = Goals_Per_Game2017(B1,B2)
    GPG3 = Goals_Per_Game2016(C1,C2)
    GPG4 = Goals_Per_Game2015(D1,D2)
    GPG5 = Goals_Per_Game2014(E1,E2)
    GPG6 = Goals_Per_Game2013(F1,F2)
    GPG7 = Goals_Per_Game2012(G1,G2)
    ListOfStats = [GPG1,GPG2,GPG3,GPG4,GPG5,GPG6,GPG7]
    Total=0
    Division=0
    for num in ListOfStats:
        if num != None:
            Total = Total + num
            Division = Division + 1
    if Division > 0:
        Shots_Factor = Total / Division
        New_Prediction = float(GPG) + Shots_Factor
        if New_Prediction < 0:
            New_Prediction = 0
        return New_Prediction
    else:
        return Backup(GPG,Age)

def Backup(GPG,AGE):
    GoalPerGame = float(GPG)
    Age = float(AGE)
    if Age < 20:
        GoalPerGame = GoalPerGame * 1.05
    elif Age > 20 and Age < 24:
         GoalPerGame = GoalPerGame * 1.1
    elif Age > 24 and Age < 30:
         GoalPerGame = GoalPerGame * 1.15
    elif Age > 30 and Age < 33:
         GoalPerGame = GoalPerGame * 0.90
    elif Age > 33 and Age < 35:
         GoalPerGame = GoalPerGame * 0.85
    elif Age > 35 and Age < 40:
         GoalPerGame = GoalPerGame * 0.80
    return GoalPerGame

def Goals_Per_Game2018(A1,A2):
    Total=0
    if len(A1)>0 and len(A2)>0:
        for player in A1:
            count=0
            while count < len(A2):
                if player[0]==A2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (A2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(A2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(A1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

def Goals_Per_Game2017(B1,B2):
    Total=0
    if len(B1)>0 and len(B2)>0:
        for player in B1:
            count=0
            while count < len(B2):
                if player[0]==B2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (B2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(B2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(B1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

def Goals_Per_Game2016(C1,C2):
    Total=0
    if len(C1)>0 and len(C2)>0:
        for player in C1:
            count=0
            while count < len(C2):
                if player[0]==C2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (C2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(C2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(C1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

def Goals_Per_Game2015(D1,D2):
    Total=0
    if len(D1)>0 and len(D2)>0:
        for player in D1:
            count=0
            while count < len(D2):
                if player[0]==D2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (D2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(D2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(D1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

def Goals_Per_Game2014(E1,E2):
    Total=0
    if len(E1)>0 and len(E2)>0:
        for player in E1:
            count=0
            while count < len(E2):
                if player[0]==E2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (E2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(E2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(E1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

def Goals_Per_Game2013(F1,F2):
    Total=0
    if len(F1)>0 and len(F2)>0:
        for player in F1:
            count=0
            while count < len(F2):
                if player[0]==F2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (F2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(F2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(F1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

def Goals_Per_Game2012(G1,G2):
    Total=0
    if len(G1)>0 and len(G2)>0:
        for player in G1:
            count=0
            while count < len(G2):
                if player[0]==G2[count][0]:
                    GPG1 = (player[5])
                    GPG2 = (G2[count][5])
                    Difference = float(GPG2) - float(GPG1)
                    Total = Total + Difference
                    count=len(G2)+1
                else:
                    count=count+1
        Increase_In_Shots=Total/len(G1)
    else:
        Increase_In_Shots=None
    return Increase_In_Shots

