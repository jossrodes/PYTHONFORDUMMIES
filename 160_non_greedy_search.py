p = 'pyyython'
non_greedy_re = 'y+?'
mymatch = re.search(non_greedy_re, p)
mymatch.group()