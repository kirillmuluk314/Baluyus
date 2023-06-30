def strcount(s):
    for i in set(s):
        count = 0
        for ssym in s:
            if i == ssym:
                count+=1
        print(i, count)
strcount()