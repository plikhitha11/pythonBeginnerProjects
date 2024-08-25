
import random
import matplotlib.pyplot as plt

def generate_password(length=12):
    # Manually define the character sets
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

    # Combine all character sets
    all_characters = letters + digits + special_characters

    # Generate the password by randomly selecting characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Generate a password
password = generate_password(length=16)

# Plot the password using matplotlib
plt.figure(figsize=(6, 3))
plt.text(0.5, 0.5, f"Generated Password:\n{password}", fontsize=14, ha='center', va='center')
plt.axis('off')  # Turn off the axis
plt.show()
