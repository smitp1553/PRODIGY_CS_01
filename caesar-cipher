def caesar_cipher(text, shift, mode):


  result = ""  # Store the result here

  for char in text:
    if char.isalpha():  # Check if it's a letter
      # Get the starting position (A for uppercase, a for lowercase)
      start = ord('A') if char.isupper() else ord('a') 

      # Calculate the shift with direction (encrypt/decrypt)
      shift_value = shift if mode == 'encrypt' else -shift

      # Calculate the new position of the letter
      new_pos = (ord(char) - start + shift_value) % 26 + start

      # Convert the new position back to a letter
      new_char = chr(new_pos)

      # Add the new character to the result
      result += new_char
    else:  # If it's not a letter, keep it as is
      result += char

  return result

# Get input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter mode (encrypt/decrypt): ")

# Encrypt or decrypt based on user input
if mode.lower() == 'encrypt':
  encrypted_message = caesar_cipher(message, shift, 'encrypt')
  print("Encrypted message:", encrypted_message)
elif mode.lower() == 'decrypt':
  decrypted_message = caesar_cipher(message, shift, 'decrypt')
  print("Decrypted message:", decrypted_message)
else:
  print("Invalid mode. Use 'encrypt' or 'decrypt'.")
