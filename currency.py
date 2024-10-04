def round_rate(rate):
    return round(rate, 4)


def reverse_rate(rate):
    if rate != 0:
        return round(1 / rate, 4)
    else:
        return 0


def format_output(date, from_currency, to_currency, rate, amount, inverse_rate):
    converted_amount = amount * rate
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate:.4f}. \n"
            f"\n So {amount:,.2f} in {from_currency} correspond to {converted_amount:,.2f} in {to_currency}. "
            f" The inverse rate was {inverse_rate:.4f}")
