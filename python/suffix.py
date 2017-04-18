import itertools;checkio=lambda w:any(f[len(f)-len(s):]==s or s[len(s)-len(f):]==f for f,s in itertools.combinations(list(w),2))

#128 character solution for http://www.checkio.org/mission/end-of-other/