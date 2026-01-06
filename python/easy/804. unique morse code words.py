class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."]

        c=''
        cc=[]
        for i in words:
            for j in i:
                a=ord(j)
                c+=code[a-97]
            cc.append(c)
            c=''
        return (len(set(cc)))
