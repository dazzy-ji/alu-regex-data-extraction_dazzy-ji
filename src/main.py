import json
import os
import re

#REGEX
#Email validation
def extract_validate_emails(text: str) -> list[dict]:
    #Regex email format
    email_format = re.compile(r'\b[A-Za-z0-9._%=-]+@[A-Za-z.-]+\.[A-Za-z]{2,}\b')
    base_emails = email_format.findall(text)

    validated_emails = []

    for email in base_emails:
        # Separating Emails based on ALU domain
        email_lower = email.lower()
        if email_lower.endswith("@alueducation.com"):
            category = "ALU Official"
        elif email_lower.endswith("@alumni.alueducation.com"):
            category = "ALU Alumni"
        elif email_lower.endswith("@si.alueducation.com"):
            category = "ALU SI"
        else:
            category = "External"

        validated_emails.append(
            {
                "email": email,
                "category": category,
                "status": "Valid"
            }
        )

    return validated_emails

#Credit Card validation and extraction
def extract_validate_credit_cards(text: str) -> list[str]:
    #Regex Patter to ensure card matches 16-digit sequences seperated by dashes, spaces or digits
    card_pattern = re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b')
    base_cards = card_pattern.findall(text)

    masked_cards = []
    for card in base_cards:
        digits_only = re.sub(r'\D', '', card)

        #Verify the card's length 
        if len(digits_only) == 16:
            masked_card = f"XXXX-XXXX-XXXX-{digits_only[-4:]}"
            masked_cards.append(masked_card)

    return masked_cards

#Phone number extraction
def extract_phone_numbers(text: str) -> list[str]:
    phone_pattern = re.compile(
        r'\b(?:\+\d{1,3}[\s.-]?)?(?:\(\d{1,4}\)|\d{1,4})[\s.-]?\d{3,4}[\s.-]?\d{3,4}\b')
    return phone_pattern.findall(text)

#URL extraction
def extract_secure_urls(text: str) -> list[str]:
    url_pattern = re.compile(r'\bhttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s"<>]*)?')
    return url_pattern.findall(text)

def main():
    input_file_path = "input/raw-text.txt"
    output_file_path = "output/sample-output.json"

    if not os.path.exists(input_file_path):
        print(f"Error: Input file missing at {input_file_path}")
        return

    with open(input_file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    final_output = {
        "emails": extract_validate_emails(raw_text),
        "credit_cards": extract_validate_credit_cards(raw_text),
        "urls": extract_secure_urls(raw_text),
        "phone_numbers": extract_phone_numbers(raw_text)
    }

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=4)

    print(f"Script executed successfully. Output saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
