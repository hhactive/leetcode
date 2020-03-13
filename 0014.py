from typing import List


class Solution:
 def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) != 0:
        tempstr = strs[0]
        l1 = len(tempstr)
        for sr in strs:
            l2 = len(sr)
            temp2 = ""
            for i in range(0, min(l1, l2), 1):
                if tempstr[i] == sr[i]:
                    temp2 = temp2 + sr[i]
                else:
                    break
            tempstr = temp2
            l1 = len(temp2)
            if tempstr == "":
                return ""
        return tempstr
    return ""


strs1 = list(['aaa', 'aa', 'aaa'])
aa=Solution()
mm=aa.longestCommonPrefix(strs1)

print(mm)
