class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nt = len(t)
        ns = len(s)

        if nt > ns:
            return ""
        hashh = {}
        for i in range(nt):
            hashh[t[i]] = hashh.get(t[i], 0) + 1
        start = 0
        end = 0
        ans = ""
        min_len = ns + 1
        window = {}
        while end < ns:
            if s[end] in hashh:
                window[s[end]] = window.get(s[end], 0) + 1
            valid = True
            for ch in hashh:
                if window.get(ch, 0) < hashh[ch]:
                    valid = False
                    break
            while valid:

                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    ans = s[start:end + 1]
                if s[start] in hashh:
                    window[s[start]] -= 1

                start += 1

        
                valid = True

                for ch in hashh:
                    if window.get(ch, 0) < hashh[ch]:
                        valid = False
                        break

            end += 1

        return ans