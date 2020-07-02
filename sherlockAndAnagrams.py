from collections import Counter
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        # print(len(s)-i+1)
        # print("i ", i)
        # print("[s[j:j+i] for j in range(len(s)-i+1)] ", [s[j:j+i] for j in range(len(s)-i+1)])
        # men generate semua substring
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        # print("a ", a)
        # menghitung semua substring yang ada di string dengan menggunakan counter
        b = Counter(a)
        print("b ", b)
        for j in b:
            print("j di for b ", j)
            print("b[j]*(b[j]-1)/2 ", b[j]*(b[j]-1)/2)
            # menghitung kombinasi dari setiap element di counter
            count+=b[j]*(b[j]-1)/2
    return int(count)

# print(sherlockAndAnagrams('abba'))
# print(sherlockAndAnagrams('abcd'))
print(sherlockAndAnagrams('ifailuhkqq'))
# print(sherlockAndAnagrams('kkkk'))
# print(sherlockAndAnagrams('cdcd'))