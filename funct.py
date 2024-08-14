def get_user_input():
    cond = True
    while cond:
        try:
            user_input = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

            if user_input not in ['A', 'B']:
                raise ValueError("Invalid input.")

            return user_input
        except ValueError as e:
            print(e)