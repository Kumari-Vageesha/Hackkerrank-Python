def count_substring(string, sub_string):
    m=len(string)
    s=len(sub_string)
    c=0
    for i in range(m-s+1):
        if(string[i:(i+s)]== sub_string):
            c=c+1
    return c

