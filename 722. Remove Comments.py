class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = "\n".join(source)
        res = []
        in_block = False
        i = 0
        start = 0

        while i < len(s):
            if not in_block and s[i:i+2] == "/*":
                if start < i:
                    res.append(s[start:i])
                in_block = True
                i += 2
                start = i

            elif in_block and s[i:i+2] == "*/":
                in_block = False
                i += 2
                start = i

            elif not in_block and s[i:i+2] == "//":
                if start < i:
                    res.append(s[start:i])
                while i < len(s) and s[i] != "\n":
                    i += 1
                start = i

            else:
                i += 1

        if not in_block and start < len(s):
            res.append(s[start:])

        final_res = [line for line in "".join(res).split("\n") if line != ""]

        return final_res
