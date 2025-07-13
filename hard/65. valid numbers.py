import re
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        pattern = re.compile(r"""^[+-]?             # optional sign
                             (                  # start group
                                 (\d+\.\d*)|    # digits then dot, optional digits
                                 (\.\d+)|       # dot then digits
                                 (\d+)          # or just digits
                             )                 
                             ([eE][+-]?\d+)?$   # optional scientific part
                          """, re.VERBOSE)
    
        return bool(pattern.match(s))