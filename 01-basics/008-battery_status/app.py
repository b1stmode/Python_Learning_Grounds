# Drill: Battery Status

# drill practicess: 
# - logical operators
# - console output
# - if/elif/e;se statemetns

#Time spent: 1.5 minutes

battery = 80

if battery < 15:
    print("Critical")
elif battery < 30:
    print("Low")
elif battery < 80:
    print("Normal")
else:
    print("Full")