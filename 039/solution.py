class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if len(candidates) == 0:
            return []
        elif len(candidates) == 1:
            if candidates[0] == target:
                return [[target]]
            
        if candidates[0] > target:
            return []
        i = 0
        while i < len(candidates):
            if i < len(candidates) -1 and candidates[i+1] <= target:
                i += 1
            else:
                break
                
        result = []
        if candidates[i] == target:
            result.append([target])
            result += self.combinationSum(candidates[:i], target)
        else:
            result += [c + [candidates[i]] for c in self.combinationSum(candidates[:i+1], target-candidates[i])]
            result += self.combinationSum(candidates[:i], target)
        return result
