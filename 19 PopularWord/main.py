from collections import Counter

words = []
while (s := input()):
    words.extend(s.split())

count = Counter(words)

m_com = count.most_common()

if len(m_com) == 1:
    print(m_com[0][0])
elif len(m_com) > 1:
    if m_com[0][1] == m_com[1][1]:
        print("---")
    else:
        print(m_com[0][0])

