from collections import defaultdict
import bisect
import math

one=open("Data/NHL2018.csv").read().splitlines()
two=open("Data/NHL2017.csv").read().splitlines()
three=open("Data/NHL2016.csv").read().splitlines()
four=open("Data/NHL2015.csv").read().splitlines()
five=open("Data/NHL2014.csv").read().splitlines()
six=open("Data/NHL2013.csv").read().splitlines()
seven=open("Data/NHL2012.csv").read().splitlines()
eight=open("Data/NHL2011.csv").read().splitlines()

new, new2, new3, new4, new5, new6, new7, new8 = [],[],[],[],[],[],[],[]
options = defaultdict(list)
ages, ages2, ages3, ages4, ages5, ages6, ages7, ages8 = [],[],[],[],[],[],[],[]

one.remove(one[0])
one.remove(one[0])
for part in one:
    m=part.split(',')
    ages.append(m[1])
    options[m[2]].append([m[0],m[1],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10],
                        m[11],m[12],m[13],m[14],m[15],m[16],m[17],m[18],m[19],
                        m[20],m[21],m[22],m[23],m[24],m[25],m[26],m[27],m[28]])
    new.append(m)
    
two.remove(two[0])
two.remove(two[0])
for part in two:
    m=part.split(',')
    ages2.append(m[1])
    new2.append(m)

three.remove(three[0])
three.remove(three[0])
for part in three:
    m=part.split(',')
    ages3.append(m[1])
    new3.append(m)

four.remove(four[0])
four.remove(four[0])
for part in four:
    m=part.split(',')
    ages4.append(m[1])
    new4.append(m)

five.remove(five[0])
five.remove(five[0])
for part in five:
    m=part.split(',')
    ages5.append(m[1])
    new5.append(m)

six.remove(six[0])
six.remove(six[0])
for part in six:
    m=part.split(',')
    ages6.append(m[1])
    new6.append(m)

seven.remove(seven[0])
seven.remove(seven[0])
for part in seven:
    m=part.split(',')
    ages7.append(m[1])
    new7.append(m)

eight.remove(eight[0])
eight.remove(eight[0])
for part in eight:
    m=part.split(',')
    ages8.append(m[1])
    new8.append(m)

def find_left(a,x): #Locate the leftmost value exactly equal to x
    i = bisect.bisect_left(a,x)
    return i

def find_right(a,x): #Locate the rightmost value exactly equal to x and return the location after that value
    i = bisect.bisect_right(a,x)
    return i

def points(x): #Find Reference Points for Year 1
    start=find_left(ages,x) 
    end=find_right(ages,x)
    return start, end

def points2(x): #Find Reference Points for Year 2
    start=find_left(ages2,x)
    end=find_right(ages2,x)
    return start, end

def points3(x): #Find Reference Points for Year 3
    start=find_left(ages3,x)
    end=find_right(ages3,x)
    return start, end

def points4(x): #Find Reference Points for Year 4
    start=find_left(ages4,x)
    end=find_right(ages4,x)
    return start, end

def points5(x): #Find Reference Points for Year 5
    start=find_left(ages5,x)
    end=find_right(ages5,x)
    return start, end

def points6(x): #Find Reference Points for Year 6
    start=find_left(ages6,x)
    end=find_right(ages6,x)
    return start, end

def points7(x): #Find Reference Points for Year 7
    start=find_left(ages7,x)
    end=find_right(ages7,x)
    return start, end

def points8(x): #Find Reference Points for Year 8
    start=find_left(ages8,x)
    end=find_right(ages8,x)
    return start, end

def collect2017(start,end,compared,position): #Returns the players with similar PPG from 2017
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new2[start][3]
            PPG=new2[start][4]
            Games=int(new2[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new2[start])
            start=start+1
    else:
        while (start!=end):
            POS=new2[start][3]
            PPG=new2[start][4]
            Games=int(new2[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new2[start])
            start=start+1
    return collectibles

def collect2016(start,end,compared,position): #Returns the players with similar PPG from 2016
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new3[start][3]
            PPG=new3[start][4]
            Games=int(new3[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new3[start])
            start=start+1
    else:
        while (start!=end):
            POS=new3[start][3]
            PPG=new3[start][4]
            Games=int(new3[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new3[start])
            start=start+1
    return collectibles

def collect2015(start,end,compared,position): #Returns the players with similar PPG from 2015
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new4[start][3]
            PPG=new4[start][4]
            Games=int(new4[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new4[start])
            start=start+1
    else:
        while (start!=end):
            POS=new4[start][3]
            PPG=new4[start][4]
            Games=int(new4[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new4[start])
            start=start+1
    return collectibles

def collect2014(start,end,compared,position): #Returns the players with similar PPG from 2015
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new5[start][3]
            PPG=new5[start][4]
            Games=int(new5[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new5[start])
            start=start+1
    else:
        while (start!=end):
            POS=new5[start][3]
            PPG=new5[start][4]
            Games=int(new5[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new5[start])
            start=start+1
    return collectibles

def collect2013(start,end,compared,position): #Returns the players with similar PPG from 2015
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new6[start][3]
            PPG=new6[start][4]
            Games=int(new6[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new6[start])
            start=start+1
    else:
        while (start!=end):
            POS=new6[start][3]
            PPG=new6[start][4]
            Games=int(new6[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new6[start])
            start=start+1
    return collectibles

def collect2012(start,end,compared,position): #Returns the players with similar PPG from 2015
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new7[start][3]
            PPG=new7[start][4]
            Games=int(new7[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new7[start])
            start=start+1
    else:
        while (start!=end):
            POS=new7[start][3]
            PPG=new7[start][4]
            Games=int(new7[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new7[start])
            start=start+1
    return collectibles

def collect2011(start,end,compared,position): #Returns the players with similar PPG from 2015
    collectibles=[]
    low=(math.floor(float(compared)*10))
    high=(math.ceil(float(compared)*10))
    low_end=low/10
    high_end=high/10

    if position=="D":
        while (start!=end):
            POS=new8[start][3]
            PPG=new8[start][4]
            Games=int(new8[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS=="D" and Games>15:
                collectibles.append(new8[start])
            start=start+1
    else:
        while (start!=end):
            POS=new8[start][3]
            PPG=new8[start][4]
            Games=int(new8[start][19])
            if float(PPG) < high_end and float(PPG) > low_end and POS!="D" and Games>15:
                collectibles.append(new8[start])
            start=start+1
    return collectibles 

def compare2018(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new[start][0]in player:
            compared.append(new[start])
        start=start+1
    return compared

def compare2017(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new2[start][0]in player:
            compared.append(new2[start])
        start=start+1
    return compared

def compare2016(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new3[start][0]in player:
            compared.append(new3[start])
        start=start+1
    return compared

def compare2015(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new4[start][0]in player:
            compared.append(new4[start])
        start=start+1
    return compared

def compare2014(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new5[start][0]in player:
            compared.append(new5[start])
        start=start+1
    return compared

def compare2013(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new6[start][0]in player:
            compared.append(new6[start])
        start=start+1
    return compared

def compare2012(start,end,people):
    player=[]
    compared=[]

    for part in people:
        player.append(part[0])

    while (start!=end):
        if new7[start][0]in player:
            compared.append(new7[start])
        start=start+1
    return compared
