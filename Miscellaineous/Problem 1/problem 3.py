def solution(N):
    
    # convert from binary to decimal
    dec = 0
    counter = len(N) - 1
    i = 0
    while counter >= 0:
        if N[counter] != "0":
            dec += 2**i
        counter -= 1
        i += 1
    
    # convert to base 6
    ans = ""
    while dec > 0:
        ans = str(dec % 6) + ans
        dec = dec // 6
    return ans

solution("100111")
solution("1111111")