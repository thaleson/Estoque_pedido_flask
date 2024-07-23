import secrets

# Gere uma chave secreta de 24 bytes e a codifique em formato hexadecimal
secret_key = secrets.token_hex(24)

print(f'Sua nova SECRET_KEY é: {secret_key}')
