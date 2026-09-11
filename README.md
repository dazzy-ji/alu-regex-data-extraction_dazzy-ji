# Data Extraction & Secure Validation Assignment

A regex based program that can extract specific types of structured data from raw text, validate input to ensure it is well-formed and does not contain unsafe or malicious content, and it also handles realistic variations of data formats as they appear in the real world.

## Main Features of the Application
-**ALU Specific Validation**: Strictly matches for '@alueducation.com', '@alumni.alueducation.com' and '@si.alueducation.com'.
-**Security Requirement**
    -**Data Privacy**: Masks credit card numbers ('****-****-****-XXXX')
    -**Sanitization**: Strips inline script tags before extraction

## Getting Started

### Requirements
- Python3 installed in your system. 

### Running the Application
Clone the repository and move to the directory:
    ```bash
    cd alu-regex-data-extration_dazzy-ji

1. Run the pyhton script
    Bash
    python3 src/main.py

2. Check the generated output inside output/sample-output.json