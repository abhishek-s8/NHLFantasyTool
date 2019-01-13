def FinalAdjustment(A,B,C,D,E,F,G,corsi,pdo,ozone,goals,assists,sp):
    Total1,Total2=0,0
    Sum1,Sum2=0,0
    count=0
    if len(A)>0:
        count=count+1
        for player in A:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(A))
        Sum2=Sum2+(Total2/len(A))
    Total1,Total2=0,0
    if len(B)>0:
        count=count+1
        for player in B:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(B))
        Sum2=Sum2+(Total2/len(B))
    Total1,Total2=0,0
    if len(C)>0:
        count=count+1
        for player in C:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(C))
        Sum2=Sum2+(Total2/len(C))
    Total1,Total2=0,0
    if len(D)>0:
        count=count+1
        for player in D:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(D))
        Sum2=Sum2+(Total2/len(D))
    Total1,Total2=0,0
    if len(E)>0:
        count=count+1
        for player in E:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(E))
        Sum2=Sum2+(Total2/len(E))
    Total1,Total2=0,0
    if len(F)>0:
        count=count+1
        for player in F:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(F))
        Sum2=Sum2+(Total2/len(F))
    Total1,Total2=0,0
    if len(G)>0:
        count=count+1
        for player in G:
            Corsi=player[12]
            PDO=player[13]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(G))
        Sum2=Sum2+(Total2/len(G))
    if count!= 0:
        Average1=Sum1/count
        Average2=Sum2/count
        CORSI=float(corsi)
        PDO=float(pdo)
        OZONE=float(ozone)
        SP=float(sp)
        New_Count=0
        if PDO < 100:
            New_Count=New_Count+1
        if OZONE > Average2:
            New_Count=New_Count+1
        if CORSI > Average1:
            New_Count=New_Count+1
        if New_Count == 3:
            goals=1.1*int(goals)
            assists=1.1*int(assists)
        elif New_Count == 2:
            goals=1.05*int(goals)
            assists=1.05*int(assists)
        else:   
            goals=int(goals)
            assists=int(assists)
    return goals,assists
    

        
            
