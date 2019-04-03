class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dic = {}
        i = 0
        for s in strs:
            sorteds = list(s)
            sorteds.sort()
            sorteds = str(sorteds)
            if sorteds in dic:
                result[dic[sorteds]].append(s)
            else:
                dic[sorteds] = i
                result.append([s])
                i += 1
        return result 
