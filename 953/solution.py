class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        t = tuple(cells)
        cache = []
        s = set()
        for k in xrange(N):
            for i in xrange(8):
                if i == 0 or i == 7:
                    tmp = cells[i]
                    cells[i] = 0
                else:
                    if tmp == cells[i+1]:
                        tmp = cells[i]
                        cells[i] = 1
                    else:
                        tmp = cells[i]
                        cells[i] = 0
            t = tuple(cells)
            if t in s:
                j = cache.index(t)
                return cache[j + (N - len(cache) - 1) % (len(cache) - j)]
            else:
                s.add(t)
                cache.append(t)
        return cells
