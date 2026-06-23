class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        sorted_text = "".join(sorted(text))
        
        max_balloons = 0
        
        for i in range(1, len(text) // 7 + 1):

            target = "".join(sorted("balloon" * i))

            text_iter = iter(sorted_text)
            if all(char in text_iter for char in target):
                max_balloons = i
            else:
                break  
                
        return max_balloons
