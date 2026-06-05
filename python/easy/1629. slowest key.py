class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        c=releaseTimes[0]
        b=keysPressed[0]
        for i in range(1,len(releaseTimes)):
            if releaseTimes[i]-releaseTimes[i-1]>c:
                c=releaseTimes[i]-releaseTimes[i-1]
                b=keysPressed[i]
            elif releaseTimes[i]-releaseTimes[i-1]==c:
                if ord(keysPressed[i])>ord(b):
                    b=keysPressed[i]
        return b

