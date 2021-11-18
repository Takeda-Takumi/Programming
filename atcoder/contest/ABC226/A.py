from decimal import Decimal,  ROUND_HALF_UP, ROUND_HALF_EVEN

x = float(input())

print(Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

