def activityNotifications(expenditure, d):
    
    # declare variable notif, and create list for store data expenditure count
    notif = 0; MAX = 200; c = [0] * (MAX+1) 
    
    for e in expenditure[:d]: c[e] += 1

    def median2(): # return 2 * median
        s = 0
        for i in range(MAX+1):
            s += c[i]
            if 2*s >= d: break
        if d % 2 == 1 or 2 * s > d: return 2*i
        # PR, baris dibawah ini belum paham
        print("i ", i)
        print(list(y for y in range(i+1,MAX+1) if c[y]))
        print("sempat kepanggil ", next( y for y in range(i+1,MAX+1) if c[y] ))
        return i + next( y for y in range(i+1,MAX+1) if c[y] )

    for i in range(d, len(expenditure)):
        if expenditure[i] >= median2() : notif += 1
        c[expenditure[i-d]] -= 1; c[expenditure[i]] += 1

    return notif

# print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 4))