# INI ADALAH MINION GAMES, INI CODE SAYA
# def minion_game(string):
#     stuart = {}
#     kevin = {}
#     vowels = ['A', 'I', 'U', 'E', 'O']

#     res = [string[i:j] for i in range(len(string))
#            for j in range(i + 1, len(string)+1)]

#     for item in res:
#         if item[0] in vowels:
#             if item in kevin:
#                 kevin[item] += 1
#             else:
#                 kevin[item] = 1
#         else:
#             if item in stuart:
#                 stuart[item] += 1
#             else:
#                 stuart[item] = 1

#     winner = 'Stuart' if sum(stuart.values()) > sum(
#         kevin.values()) else 'Kevin' if sum(stuart.values()) < sum(
#         kevin.values()) else 'Draw'
#     value = max(sum(stuart.values()), sum(kevin.values()))

#     if winner == 'Draw':
#         print('Draw')
#     else:
#         print(winner, value)


def minion_game(s):

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        print('i ', i)
        print('s[i] ', s[i])
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


print(minion_game('BANANA'))
# print(minion_game('BANANANAAAS'))
