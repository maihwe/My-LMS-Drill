""" Implement vote_eligibility(age, country). Return Eligible if age is at least 18 and country is Nigeria. Otherwise return Not eligible. The country check should be case-insensitive and should ignore leading and trailing spaces."""
def vote_eligibility(age, country):
    country = country.strip().lower()

    if age >= 18 and country == "nigeria":
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print(vote_eligibility(20, "Nigeria"))
print(vote_eligibility(18, "  NIGERIA  "))
print(vote_eligibility(17, "Nigeria"))
print(vote_eligibility(25, "Ghana"))