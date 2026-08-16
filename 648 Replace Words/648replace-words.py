class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hashh = set(dictionary)
        words = sentence.split()
        ans = []

        for word in words:
            root = word

            for i in range(1, len(word) + 1):
                if word[:i] in hashh:
                    root = word[:i]
                    break

            ans.append(root)

        return " ".join(ans)