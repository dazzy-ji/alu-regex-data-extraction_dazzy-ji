# Data Extraction & Secure Validation Assignment

A regex based program that can extract specific types of structured data from raw text, validate input to ensure it is well-formed and does not contain unsafe or malicious content, and it also handles realistic variations of data formats as they appear in the real world.

## Main Features of the Application
- **ALU Specific Validation**: Strictly matches for '@alueducation.com', '@alumni.alueducation.com' and '@si.alueducation.com'.
- **Security Requirement**
    - **Data Privacy**: Masks credit card numbers ('****-****-****-XXXX')
    - **Sanitization**: Strips inline script tags before extraction
    - **Correctness**: Ensures that the phone number entered is valid

## Getting Started

### Requirements
- Python3 installed in your system. 

### Running the Application
```bash
1. Clone the repository and move to the directory:
    cd alu-regex-data-extration_dazzy-ji

2. Run the python script
    Bash
    python3 src/main.py

3. Check the generated output inside output/sample-output.json