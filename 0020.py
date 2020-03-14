class Solution:
    def isValid(self, s: str) -> bool:
        ss=''
        for i in s:
            ss=ss+i
            if len(ss)>1 and (i==')' or i==']' or i=='}'):
                if i==')' and ss[-2]!='(':
                    return False
                if i==']' and ss[-2]!='[':
                    return False
                if i=='}' and ss[-2]!='{':
                    return False
                ss=ss[:-2]
        if len(ss)==0:
            return True


str1='{[]}'
aa=Solution()
mm=aa.isValid(str1)

print(mm)