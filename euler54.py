p1=[]
p2=[]
order={'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
ranks={'ROYAL':10,
       'STRAIGHT-FLUSH':9,
       'FOUR-KIND':8,
       'FULL-HOUSE':7,
       'FLUSH':6,
       'STRAIGHT':5,
       'THREE-KIND':4,
       'TWO-PAIR':3,
       'PAIR':2,
       'HIGH':1
}
for line in open('euler54_r.txt'):
    i=line.split()
    p1.append([i[0],i[1],i[2],i[3],i[4]])
    p2.append([i[5],i[6],i[7],i[8],i[9]])
def sort(toSort):
    suite={}
    for i in toSort:
        if i[1] not in suite:
            suite[i[1]]=[i[0]]
        else:
            suite[i[1]].append(i[0])
    card={}
    for j in toSort:
        if order[j[0]] not in card:
            card[order[j[0]]]=[j[1]]
        else:
            card[order[j[0]]].append(j[1])
    return suite,card
def rank(hand):
    r=''
    p=0
    s,c=sort(hand)
    k=sorted(c.keys())[::-1]
    v=c.values()
    flush=False
    straight=False
    if len(s)==1:
        flush=True
    if len(c)==5 and k[0]-k[4]==4:
        straight=True
    if straight==True and flush==True:
        if k[0]==13:
            r='ROYAL'
        else:
            r='STRAIGHT-FLUSH'
    elif len(c)==2:
        if len(v[0])==4:
            r='FOUR-KIND'
            p=c.keys()[0]
        elif len(v[1])==4:
            r='FOUR-KIND'
            p=c.keys()[1]
        else:
            r='FULL-HOUSE'
            if len(v[0])==3:
                p=[c.keys()[0],c.keys()[1]]
            else:
                p=[c.keys()[1],c.keys()[0]]
    elif flush==True:
        r='FLUSH'
    elif straight==True:
        r='STRAIGHT'
    else:
        pairs=0
        for l in v:
            if len(l)==2:
                pairs+=1
        if pairs==2:
            r='TWO-PAIR'
            p=[]
            for a in range(0,len(c.keys())):
                if len(v[a])==2:
                    p.append(c.keys()[a])
            p=sorted(p)[::-1]
        elif pairs==1:
            r='PAIR'
            for a in range(0,len(c.keys())):
                if len(v[a])==2:
                    p=c.keys()[a]
                    break
        for l in v:
            if len(l)==3:
                r='THREE-KIND'
                for a in range(0,len(c.keys())):
                    if len(v[a])==3:
                       p=c.keys()[a]
                       break
                break
        if r!='TWO-PAIR' and r!='PAIR' and r!='THREE-KIND':
            r='HIGH'
    
    cv=[]
    for x in range(0,len(c.keys())):
        for y in range(0,len(c.values()[x])):
            cv.append(c.keys()[x])
    cv=sorted(cv)[::-1]
    
    return r,cv,p

p1wins=0
p2wins=0
for games in range(0,len(p1)):
    win=0
    t1=rank(p1[games])
    t2=rank(p2[games])
    if ranks[t1[0]]>ranks[t2[0]]:
        win=1
    elif ranks[t1[0]]==ranks[t2[0]]:
        pr=False
        if t1[0]==('TWO-PAIR' or 'FULL-HOUSE'):
            if t1[2][0]>t2[2][0]:
                win=1
                pr=True
            elif t1[2][0]<t2[2][0]:
                win=2
                pr=True
            elif t1[2][0]==t2[2][0]:
                if t1[2][1]>t2[2][1]:
                    win=1
                    pr=True
                elif t1[2][0]<t2[2][0]:
                    win=2
                    pr=True
        elif t1[0]==('PAIR' or 'THREE-KIND' or 'FOUR-KIND'):
            if t1[2]>t2[2]:
                win=1
                pr=True
            elif t1[2]<t2[2]:
                win=2
                pr=True
        if pr==False:
            for crds in range(0,len(t1[1])):
                if t1[1][crds]>t2[1][crds]:
                    win=1
                    break
                elif t1[1][crds]<t2[1][crds]:
                    win=2
                    break
    else:
        win=2
    if win==1:
        p1wins+=1
    elif win==2:
        p2wins+=1
    print(t1,t2,win)
print(p1wins,p2wins)
