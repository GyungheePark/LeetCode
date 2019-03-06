int lengthOfLongestSubstring(char* s) {
    int i = 0;
    int j;
    int result = 0;
    bool seen[256];
    while (s[i] != '\0') {
        memset(seen, false, sizeof(seen));
        j = i;
        while (s[j] != '\0') {
            if (seen[s[j]]) {
                break;
            } else {
                seen[s[j]] = true;
                j++;
                result = result < j-i? j-i : result;
            }
        }
        i++;
    }
    return result;
}
