'''
2次元の表をリストで表す
'''

Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalent = [['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'], ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code']]


def Hire4Show(Candidates, Talents, CandidateTalent):
    '''
    全てのTalentを含むようなCandidateの組み合わせを全通り作成する。
    '''
    hire = Candidates
    n = len(Candidates)
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                Combination = Combination + [Candidates[n - j - 1]]
            num = num // 2
        if (Good(Combination, Candidates, Talents, CandidateTalent) == True):
            if (len(hire) > len(Combination)):
                hire = Combination
    print('good Combination:', hire)

def Good(Combination, Candidates, Talents, CandidateTalent):
    cover = False
    tal = set()
    for cand in Combination:
        #print(cand)
        tal = tal.union(CandidateTalent[Candidates.index(cand)])
    #print(tal)
    if (len(tal) == len(Talents)):
        return True
    else:
        return False

Hire4Show(Candidates, Talents, CandidateTalent)
