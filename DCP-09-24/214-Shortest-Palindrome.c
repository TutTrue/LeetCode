int isPali(char *s, int r) {
    int l = 0;
    while (l <= r) {
        if (s[l] != s[r]) return 0;
        l+=1;
        r-=1;
    }
    return 1;
}
char* shortestPalindrome(char* s) {
    int len = strlen(s);
    int i = len -1;
    for (; i > -1; i--) {
        if (isPali(s, i)) {
            char *tmp = (char *)malloc(len - i + len);
            int j = 0, k = len - 1;
            while (k > i) {
                tmp[j] = s[k];
                j++;
                k--;
            }
            k = 0;
            while (s[k] != '\\0') {
                tmp[j] = s[k];
                j++;
                k++;
            }
            tmp[j] = '\\0';
            return tmp;
        }
    }
    return \\;
}