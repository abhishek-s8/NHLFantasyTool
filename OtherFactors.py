def FinalAdjustment(A,B,C,D,E,F,G,corsi,pdo,ozone,goals,assists):
    
    Total1,Total2=0,0 #The sum of Player Corsi and Ozone in that specific season
    Sum1,Sum2=0,0 #The sum of ALL players Corsi and Ozone from EVERY season 
    count=0 #Counts the total number of seasons that has compareables
    
    if len(A)>0: #If there are compareable player's in respective season
        count=count+1
        for player in A:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(A))
        Sum2=Sum2+(Total2/len(A))
        
    Total1,Total2=0,0 #Reset values for next comparison
    
    if len(B)>0: #If there are compareable player's in respective season
        count=count+1
        for player in B:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(B))
        Sum2=Sum2+(Total2/len(B))
        
    Total1,Total2=0,0 #Reset values for next comparison
    
    if len(C)>0: #If there are compareable player's in respective season
        count=count+1
        for player in C:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(C))
        Sum2=Sum2+(Total2/len(C))
        
    Total1,Total2=0,0 #Reset values for next comparison
    
    if len(D)>0: #If there are compareable player's in respective season
        count=count+1
        for player in D:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(D))
        Sum2=Sum2+(Total2/len(D))
        
    Total1,Total2=0,0 #Reset values for next comparison
    
    if len(E)>0: #If there are compareable player's in respective season
        count=count+1
        for player in E:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(E))
        Sum2=Sum2+(Total2/len(E))
        
    Total1,Total2=0,0 #Reset values for next comparison
    
    if len(F)>0: #If there are compareable player's in respective season
        count=count+1
        for player in F:
            Corsi=player[12]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(F))
        Sum2=Sum2+(Total2/len(F))
        
    Total1,Total2=0,0 #Reset values for next comparison
    
    if len(G)>0: #If there are compareable player's in respective season
        count=count+1
        for player in G:
            Corsi=player[12]
            PDO=player[13]
            OZone=player[14]
            Total1=Total1+float(Corsi)
            Total2=Total2+float(OZone)
        Sum1=Sum1+(Total1/len(G))
        Sum2=Sum2+(Total2/len(G))
        
    if count!= 0: #If there are any season with compareables
        Average1=Sum1/count
        Average2=Sum2/count
        CORSI=float(corsi)
        PDO=float(pdo)
        OZONE=float(ozone)
        New_Count=0 #Counts the number of times if statement is true
        
        if PDO < 100: #If PDO less than average amount
            New_Count=New_Count+1
        if OZONE > Average2: #If Ozone Starts higher than average amount
            New_Count=New_Count+1
        if CORSI > Average1: #If Corsi higher than average amount
            New_Count=New_Count+1
        if New_Count == 3: #If all 3 are true increase estimate
            goals=1.1*int(goals)
            assists=1.1*int(assists)
        elif New_Count == 2: #If all 2 are true increase estimate
            goals=1.05*int(goals)
            assists=1.05*int(assists)
        else:   #Keep estimate as it is
            goals=int(goals)
            assists=int(assists)
            
    else: #If there wasn't any compareables
        CORSI=float(corsi)
        PDO=float(pdo)
        OZONE=float(ozone)
        New_Count=0 #Counts the number of times if statement is true
        
        if PDO < 100: #If PDO less than average amount
            New_Count=New_Count+1
        if OZONE > 50: 
            New_Count=New_Count+1
        if CORSI > 0: 
            New_Count=New_Count+1
        if New_Count == 3: #If all 3 are true increase estimate
            goals=1.1*int(goals)
            assists=1.1*int(assists)
        elif New_Count == 2: #If all 2 are true increase estimate
            goals=1.05*int(goals)
            assists=1.05*int(assists)
        else:   #Keep estimate as it is
            goals=int(goals)
            assists=int(assists)
            
    return goals,assists
    

        
            
