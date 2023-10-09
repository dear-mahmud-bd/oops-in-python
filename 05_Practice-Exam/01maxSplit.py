# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S

str = input()
blncd_strs = []  
curr_str = ""    
blnc_cnt = 0      
for ch in str:
    curr_str += ch
    if ch == 'L': blnc_cnt += 1
    else: blnc_cnt -= 1
    if blnc_cnt == 0:
        blncd_strs.append(curr_str)
        curr_str = ""
print(len(blncd_strs))
for blncd_str in blncd_strs:
    print(blncd_str)