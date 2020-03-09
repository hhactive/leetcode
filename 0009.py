class Solution:
    def isPalindrome(self, x: int) -> bool:
        tem=x
        rev=0
        if x>=0:
          while (tem>0):
            re=tem%10
            rev=(rev*10)+re
            tem=tem//10
          if(x==rev):
            return True
          else:
            return False
        else:
            return False