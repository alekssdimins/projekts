import os
import fitz  # PyMuPDF

def extract_payment_info(text):
    name_pattern = "Vārds uzvārds/ name:"
    amount_pattern = "Maksājuma Summa/ amount of payment:"
    recipient_pattern = "Nosaukums/ beneficiary’s data:"

    name_start = text.find(name_pattern) + len(name_pattern)
    name_end = text.find('\n', name_start)
    name = text[name_start:name_end].strip() if name_start != -1 and name_end != -1 else None

    amount_start = text.find(amount_pattern) + len(amount_pattern)
    amount_end = text.find('\n', amount_start)
    amount = text[amount_start:amount_end].strip() if amount_start != -1 and amount_end != -1 else None

    recipient_start = text.find(recipient_pattern) + len(recipient_pattern)
    recipient_end = text.find('\n', recipient_start)
    recipient = text[recipient_start:recipient_end].strip() if recipient_start != -1 and recipient_end != -1 else None

    return name, recipient, amount

def process_payment_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)

            doc = fitz.open(pdf_path)
            text = ""
            for page_num in range(doc.page_count):
                page = doc[page_num]
                text += page.get_text()

            print(f"PDF: {filename}")
            print(f"Extracted text from {filename}:\n{text}")

            name, recipient, amount = extract_payment_info(text)

            print(f"PAYMENT FROM: {name}")
            print(f"PAYMENT TO: {recipient}")
            print(f"PAYMENT AMOUNT: {amount}")
            print("\n" + "-"*30 + "\n")

# Specify the directory containing your PDF files
process_payment_files('/Users/alekssdimins/Desktop/projekts')
