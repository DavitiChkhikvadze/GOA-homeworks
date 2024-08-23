#What's the real floor?
def get_real_floor(n):
    if n > 13:
        return n - 2
    elif n <= 0:
        return n
    else:
        return n - 1
    
#Holiday VIII - Duty Free
def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * (discount / 100))

#Credit card issuer checking
def get_issuer(number):
    new_string = str(number)
    if len(new_string) == 15 and new_string[0] == '3':
        return 'AMEX'
    elif len(new_string) == 16 and new_string[3:] == '6011':
        return 'Discover'
    elif (len(new_string) == 13 or 16) and new_string[0] == '4':
        return 'VISA'
    elif len(new_string) == 16 and new_string[0] == '5':
        return 'Mastercard'
    else:
        return 'Unknown'
#danarcheni ver gavakete

 

    
