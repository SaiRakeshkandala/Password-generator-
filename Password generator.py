import random
import string

def generate_password(length):
    if length < 4:
        print("❌ Password length should be at least 4.")
        return None
    
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one character from each pool
    all_characters = lower + upper + digits + special
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)
    
    # Fill the remaining length with random characters
    password += ''.join(random.choices(all_characters, k=length-4))
    
    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))
    return password

def main():
    print("🔒 Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    
    password = generate_password(length)
    if password:
        print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
