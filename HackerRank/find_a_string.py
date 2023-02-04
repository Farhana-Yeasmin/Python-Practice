string ="ABCDCDC"
sub_string = "CDC"

# string[2:6]
# A B C D CDC

# ABC FALSE
# BCD FALSE
# CDC TRUE
# DCD False
# CDC True

def count_substring(string, sub_string):
    
    cnt = 0
    length = (len(string) - (len(sub_string)-1))
    
    for i in range(0,length):
        sub = string[i:len(sub_string)+i]
        if sub == sub_string:
            cnt = cnt + 1
    return cnt        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)