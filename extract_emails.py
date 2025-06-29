import re

# Step 1: Read input file
input_file = "input_text.txt"  # replace with your actual file
output_file = "extracted_emails.txt"

try:
    with open(input_file, 'r') as file:
        text = file.read()

    # Step 2: Extract emails using regex
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)

    # Step 3: Save to output file
    with open(output_file, 'w') as out_file:
        for email in emails:
            out_file.write(email + '\n')

    print(f"✅ {len(emails)} email(s) extracted and saved to '{output_file}'.")

except FileNotFoundError:
    print("❌ Input file not found. Make sure 'input_text.txt' exists.")