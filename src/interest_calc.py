def interest_calculator(amount, rate, time):
    """
    This is simple interest calculated solely on the initial principal amount.
    
    :param amount: Principal amount
    :param rate: Interest rate 
    :param time: Time period in years only.
    """

    simple_interest = (amount * rate * time) / 100
    return f"Simple Interest: {simple_interest:.2f}"
