import pillod

print("=== Pillod Library Demo ===\n")

# Demo of parsertools
number = pillod.parsertools.ask_int("Enter a number between 1 and 10: ", 1, 10)
print(f"You entered: {number}")

# Math tools demo
print(f"\nMath tools:")
print(f"  {number} factorial = {pillod.mathtools.factorial(number)}")
print(f"  Is {number} prime? {pillod.mathtools.is_prime(number)}")
print(f"  First {number} Fibonacci numbers: {pillod.mathtools.fibonacci(number)}")

# Demo of yes/no question
if pillod.parsertools.ask_yes_no("\nDo you want to see more examples?"):
    # Random tools demo
    print(f"\nRandom tools:")
    print(f"  Random password: {pillod.randomtools.random_password()}")
    print(f"  Random hex color: {pillod.randomtools.random_hex_color()}")
    print(f"  Coin flip: {pillod.randomtools.coin_flip()}")
    print(f"  Dice roll: {pillod.randomtools.dice_roll()}")
    
    # List tools demo
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print(f"\nList tools (input: {sample_list}):")
    print(f"  Remove duplicates: {pillod.listtools.remove_duplicates(sample_list)}")
    print(f"  Chunk by 2: {pillod.listtools.chunk_list(sample_list, 2)}")
    
    # String utilities demo
    text = "hello world"
    print(f"\nString tools (input: '{text}'):")
    print(f"  Title Case: {pillod.stringtools.to_title_case(text)}")
    print(f"  Snake Case: {pillod.stringtools.to_snake_case('HelloWorld')}")
    print(f"  Word Count: {pillod.stringtools.count_words(text)}")
    print(f"  Reversed: {pillod.stringtools.reverse_string(text)}")
    
    # Validators demo
    print(f"\nValidators:")
    test_email = "test@example.com"
    print(f"  Is '{test_email}' valid email? {pillod.validators.is_email(test_email)}")
    test_url = "https://github.com"
    print(f"  Is '{test_url}' valid URL? {pillod.validators.is_url(test_url)}")
    
    # Date tools demo
    print(f"\nDate tools:")
    print(f"  Current date: {pillod.datetools.current_date()}")
    print(f"  Current time: {pillod.datetools.current_time()}")
    print(f"  Random date: {pillod.randomtools.random_date()}")

print("\n=== Demo Complete ===")
