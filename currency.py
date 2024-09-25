def format_currency(amount, currency_code):
    return f"{amount:,.2f} {currency_code}"


def round_rate(rate):
    return round(rate, 4)


def reverse_rate(rate):
    if rate != 0:
        return round(1 / rate, 4)
    else:
        return 0


def format_output(date, from_currency, to_currency, rate, amount):
    converted_amount = amount * rate
    return (f"On {date}, {amount:,.2f} {from_currency} was equal to "
            f"{converted_amount:,.2f} {to_currency} at a rate of {rate:.4f}.")
