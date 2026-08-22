# Drill: Entry Consent

# drill practicess: 
# - logical operators
# - console output

#Time spent: 40 seconds
age = 16
has_parent = True
has_permission = False

can_enter = (age >= 18 or age < 18 and has_parent) and has_permission
print(can_enter)