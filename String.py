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