def minimumBribes(q):
    newQ = [el - 1 for el in q]
    moves = 0
    for i, item in enumerate(newQ):
        if item - i > 2:
            return "Too chaotic"

        # ini penjelasan yg nemu solusi di hackerrank, sebuah solusi yang sangat brilian

        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front of P's original position,
        # so we need to look from one position in front # <- ini terkena aturan bahwa setiap orang hanya dapat menyuap orang di depannya maksimal dua kali
        # of P's original position to one in front of P's
        # current position, and see how many of those
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(item-1, 0), i):
            if newQ[j] > item:
                moves += 1

    return moves


# print(minimumBribes([2, 1, 5, 3, 4]))
# print(minimumBribes([2, 5, 1, 3, 4]))
print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
