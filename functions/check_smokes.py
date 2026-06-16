def check_smokes(daily_smokes):
    if daily_smokes >= 20:
        return "High"
    elif daily_smokes >= 10:
        return "Moderate"
    else:
        return "Low"
print(check_smokes(15.5))