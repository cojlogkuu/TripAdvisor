# Open the file and print its contents, showing any non-printable characters
# with open('D:/projects/TripAdvisor/app/auth/domain/models.py', 'rb') as file:
#     content = file.read()
#     print(content)

with open('D:/projects/TripAdvisor/app/auth/domain/models.py', 'rb') as file:
    content = file.read()

# Replace null bytes
clean_content = content.replace(b'\x00', b'')  # Remove null bytes

# Write the clean content back to the file
with open('D:/projects/TripAdvisor/app/auth/domain/models.py', 'wb') as file:
    file.write(clean_content)

# with open('D:/projects/TripAdvisor/app/auth/domain/models.py', 'r', encoding='utf-8') as file:
#     content = file.read()
