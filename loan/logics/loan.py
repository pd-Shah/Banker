

def calculate_monthly_refund(loan_value, profit, total_months,):
    try:
        value = loan_value*((profit/2)+0.5)/total_months

    except:
        value = 0

    return value
