def make_sandwich(*items):
    print("\n Your sandwich:")
    for item in items:
        print(f"...add {item} to your sandwich.")
    print("Sandwich is ready!")


make_sandwich('beef', 'swiss cheese', 'lettuce')
make_sandwich('peanut butter', 'nutella')