class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        parts = date.split(" ")  
        day = parts[0][:-2].zfill(2)                      
        month = str(months.index(parts[1]) + 1).zfill(2)  
        year = parts[2]                                  

        return "{}-{}-{}".format(year, month, day)
