#award.py

print("This program will determine your award for the triathalon.")

# Collecting user input for each event
try:
    running = int(input("Please enter the number of minutes it took you to complete the running event: "))
    cycling = int(input("Please enter the number of minutes it took you to complete the cycling event: "))
    swimming = int(input("Please enter the number of minutes it took you to complete the swimming event: "))

    # Calculating total time
    total = running + cycling + swimming

    # Determining the award based on the total time
    if total <= 100:
        print("Congratulations! You have been awarded Honorary Colours.")
    elif 101 <= total <= 105:
        print("Congratulations! You have been awarded Honorary Half Colours.")
    elif 106 <= total <= 110:
        print("Congratulations! You have been awarded Honorary Scroll.")
    else:
        print("Unfortunately, you have not qualified for an award this time.")

except ValueError:
    print("Please enter valid numerical values for the times.")