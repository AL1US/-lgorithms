# Так себе решение изза использования встроенной функции
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array1 = []
        array2 = []

        for i in s:
            array1.append(i)
        
        for i in t:
            array2.append(i)

        ar1 = sorted(array1)
        ar2 = sorted(array2)

        if ar1 == ar2:
            return True
            
        return False

# дальше решение от ии
    
# Best
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# через словарь
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1 # 0 - значение по умолчанию, которое нужно вернуть если там пусто

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True    