print ''.join([''.join(e+list(reversed(e))) for e in [[unichr(x+i) for x in [97,65,12354,12450]] for i in range(26)]])