#print (''.join([i.lower() if i.isupper() else i.upper() for i in input()]))
#print(*map(lambda ch : ch.lower() if ch.isupper() else ch.upper(), input()), sep="")

def swap_case(s):
    return s.swapcase()
