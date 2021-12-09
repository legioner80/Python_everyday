favorite_numbers = {
    'andrei': [33, 9],
    'erika': [3, 99, 1111],
    'ivan': [99, 88, 4444555]
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()} likes the following numbers:")
    for number in numbers:
        print(f" {str(number)}")
