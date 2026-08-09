class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
           
            res.append( str(len(s)) + "#" + s)

        return "".join(res)
            
            
                





    def decode(self, s: str) -> List[str]:
        i = 0
        add = []
        op = [] 
        
        while i< len(s):
            num = 0
            j = i
            
            while s[j] != '#':
                
                num = num*10 + int(s[j])
                j +=1
            i = j+1    
            while num > 0 :
                add.append(s[i])
                i += 1 
                num -= 1
            op.append("".join(add))
            add =[]
            
        return op
                