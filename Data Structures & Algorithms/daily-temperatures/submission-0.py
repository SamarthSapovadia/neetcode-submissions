class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        for temp_today in range(len(temperatures)):
            temp = temperatures[temp_today]
            flag=True
            for future_temp in range(temp_today,len(temperatures)):
                if temp < temperatures[future_temp]:
                    days.append((future_temp-temp_today))
                    flag=False
                    break
            if flag:
                days.append(0)
        return days