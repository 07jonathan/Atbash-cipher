def atbash_cipher_decrypt(cipher_text):
    # Create the translation table for Atbash Cipher
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet + alphabet.lower(), reversed_alphabet + reversed_alphabet.lower())
    
    # Decrypt the cipher text using the translation table
    decrypted_text = cipher_text.translate(translation_table)
    return decrypted_text

# Example usage
cipher_text = "GSRH RH Z HVXIVG"
decrypted_text = atbash_cipher_decrypt(cipher_text)
print(f"Cipher Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
