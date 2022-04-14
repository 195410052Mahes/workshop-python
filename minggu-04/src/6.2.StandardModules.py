import sys
sys.ps1
# '>>> ' (Output)

>>> sys.ps2
# '... ' (Output)

>>> sys.ps1 = 'C> '
# C> print('Yuck!') (Output)
# Yuck! (Output)
# C> (Output)

import sys
sys.path.append('/ufs/guido/lib/python')