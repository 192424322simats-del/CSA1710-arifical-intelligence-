def vacuum_cleaner():

    # Initial state
    location = "A"
    room_A = "Dirty"
    room_B = "Dirty"

    print("Initial State:")
    print("Location:", location)
    print("Room A:", room_A)
    print("Room B:", room_B)
    print()

    # Clean Room A
    if location == "A" and room_A == "Dirty":
        print("Vacuum cleans Room A")
        room_A = "Clean"

    # Move to Room B
    print("Vacuum moves from A to B")
    location = "B"

    # Clean Room B
    if location == "B" and room_B == "Dirty":
        print("Vacuum cleans Room B")
        room_B = "Clean"

    print()

    # Final state
    print("Final State:")
    print("Location:", location)
    print("Room A:", room_A)
    print("Room B:", room_B)


# Main program
vacuum_cleaner()
