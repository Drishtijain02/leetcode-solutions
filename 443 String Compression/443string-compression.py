class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0

        while i < len(chars):
            count = 1

            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
                i += 1

            s += chars[i]

            if count > 1:
                s += str(count)

            i += 1

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)