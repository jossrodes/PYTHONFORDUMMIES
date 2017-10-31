import decimal
decimal.getcontext()
decimal.getcontext().prec = 7
data = Decimal('7.324')
data.quantize(Decimal('.01'))