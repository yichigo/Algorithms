class Solution:
    def compress(self, chars: List[str]) -> int:
        i_write = 0
        count = 0
        for char in chars:
            if char == chars[i_write]:
                count += 1
            else:
                if count > 1:
                    for digit in str(count):
                        i_write += 1
                        chars[i_write] = digit
                
                i_write += 1
                chars[i_write] = char
                count = 1
        
        if count > 1:
            for digit in str(count):
                i_write += 1
                chars[i_write] = digit
        
        return i_write + 1

    def isStrobogrammatic(self, num: str) -> bool:
        flip = {'0':'0','1':'1','6':'9', '8':'8', '9':'6'}
        
        n = len(num)
        for i in range(ceil(n/2)):
            if (num[i] in flip) and (flip[num[i]] == num[n-1-i]):
                continue
            else:
                return False
        
        return True

    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2