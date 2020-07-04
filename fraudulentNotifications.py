def activityNotifications(expenditure, d):

    notif = 0 ; MAX = 200 ; c = [0] * (MAX+1)
    for e in expenditure[:d] : c[e] += 1

    def median2(): # returns twice the median
        s = 0
        for x in range(MAX+1):
            s += c[x]
            if 2*s >= d : break
        if d%2 == 1 or 2*s > d : return 2*x
        return x + next( y for y in range(x+1,MAX+1) if c[y] )

    for i in range(d,len(expenditure)):
        if expenditure[i] >= median2() : notif += 1
        c[expenditure[i-d]] -= 1 ; c[expenditure[i]] += 1        
    return notif

print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))