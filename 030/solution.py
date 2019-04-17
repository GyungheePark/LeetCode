class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        wordnum = len(words)
        if wordnum == 0:
            return []
        wordlen = len(words[0])
        result = []
        for i in range(len(s)):
            if i <= len(s) - (wordnum * wordlen):
                dic = {}
                for word in words:
                    if word in dic:
                        dic[word] += 1
                    else:
                        dic[word] = 1
                isSubstring = True
                for j in range(wordnum):
                    subs = s[i+j*wordlen:i+(j+1)*wordlen]
                    if subs in words and subs in dic and dic[subs] > 0:
                        dic[subs] -= 1
                    else:
                        isSubstring = False
                        break
                if isSubstring:
                    result.append(i)
            else:
                break
        return result


