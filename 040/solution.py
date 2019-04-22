class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if not candidates:
            return []
        if len(candidates) == 1:
            if candidates[0] == target:
                return [[target]]
            else:
                return []
        
        i = 0
        while i < len(candidates):
            if i+1 < len(candidates) and candidates[i+1] <= target:
                i += 1
            else:
                break
        result = []
        if candidates[i] == target:
            result.append([target])
            for c in self.combinationSum2(candidates[:i], target):
                if not c in result:
                    result.append(c)
        else:
            for c in self.combinationSum2(candidates[:i], target-candidates[i]):
                c.append(candidates[i])
                if c not in result:
                    result.append(c)
            for c in self.combinationSum2(candidates[:i], target):
                if c not in result:
                    result.append(c)
        return result
        
