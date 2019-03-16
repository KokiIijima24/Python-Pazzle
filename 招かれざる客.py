'''
リストの連結
しらみつぶしの数え上げと符号化の組み合わせ
[] 00000
[a b] 11000
[a b c] 11100
あるかないかを２進数で表現することによって全ての組み合わせ
を符号化によって作成する。
'''
guestList = ['A', 'B', 'C', 'D', 'E']
disLikePairs = [['A', 'B'], ['A', 'C']]

def Combination(n, guestList):
    allCombL = []
    for i in range(2**n):
        cList = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                cList = cList + [guestList[n - j - 1]]
            num = num // 2
        allCombL.append(cList)
    return allCombL

comb = Combination(5, guestList)

def removeBadCombination(allCombL, disLikePairs):
    allGoodCombinations = []
    for i in allCombL:
        for j in disLikePairs:
            good = True
            if (j[0] in i and j[1] in i):
                good = False
            if good:
                allGoodCombinations.append(i)
    return allGoodCombinations

def InviteDinner(guestList, disLikePairs):
    #allCombL = Combination(len(guestList), guestList)
    #allGoodCombinations = removeBadCombination(allCombL, disLikePairs)
    allGoodCombinations = largeSol([], guestList, disLikePairs, [])
    invite = []
    invite = allGoodCombinations
    print('一番良い組み合わせは、', invite, 'です。')

# 再帰関数を使ったプログラム
def largeSol(choosen, guestList, disLikePairs, Sol):
    if (len(guestList) == 0):
        if (Sol == [] or len(choosen) > len(Sol)):
            Sol = choosen
        return Sol
    if (removeBadCombination(choosen + [guestList[0]], disLikePairs)):
        Sol = largeSol(choosen + [guestList[0]], guestList[1:], disLikePairs, Sol)
    return largeSol(choosen, guestList[1:], disLikePairs, Sol)


InviteDinner(guestList, disLikePairs)
