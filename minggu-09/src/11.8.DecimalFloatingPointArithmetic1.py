Decimal('1.00') % Decimal('.10')
# Decimal('0.00') (Output)
1.00 % 0.10
# 0.09999999999999995 (Output)

sum([Decimal('0.1')]*10) == Decimal('1.0')
# True (Output)
sum([0.1]*10) == 1.0
# False (Output)