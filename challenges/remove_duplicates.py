raw_guests = ["Alex", "Jordan", "Taylor", "Alex", "Morgan", "Jordan", "Charlie"]
def clean_guestlist(names_list):
    return list(set(names_list))
cleaned_guests = clean_guestlist(raw_guests)
print(cleaned_guests)