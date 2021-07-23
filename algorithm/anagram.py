# アナグラム

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram('iceman', 'cinema'))
print(anagram('leaf', 'tree'))

# 文字列内に出現するCharの出現回数をカウントする
# collections
from collections import defaultdict

def count_characters(str):
    c_dict = defaultdict(int)
    for c in str:
        c_dict[c] += 1
    print(c_dict)

count_characters('Dynasty')

# collections.Counter
from collections import Counter
print(Counter('Dynasty'))
