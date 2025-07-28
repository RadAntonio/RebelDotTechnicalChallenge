from pdfreader import SimplePDFViewer
import re

# pentru a extrage datele din tabel m am gandit sa extract tabelul din pdf stiind ca incepe dupa INV-XXXX si deacolo sa merg in 4 in 4 pentru o line a produsului, si as as stii care sunt positiile pentru cantitate, pret unitar si total iar mai apoi as putea
# sa fac calcul pentru a vedea daca totalulu final da la fel cu totalul adunat din iteme

# pentru a exy=trage data ma gandeam tot la un regex ori sa folosesc datetime pentru validare

# iar pentru punctul 4 ma gandeam sa folosesc pydantic pentru a formata intr un JSON obiectele create de tip clasa InvoiceData

# thought process-ul: identificare format PDF-uri  si potentiale probleme e.g. romana vs engleza, diacritice"?" , text adaugat la final(invoice romana)
                      # extragere date - regex pentru data si invoice number + observat unde incepe tabelul
                      # definit clasa (atribute: inv. nr, data, item type(list) [pret unitar, cantitate, total])
                      # validare date tabel (testare functii)
                      # exportare format JSON
                      # extindere la mai multe pdf + citire autmata prin a da doar un folder ca input

# Va multumesc pentru oportunitate :)

fd = open("./Invoices/invoice_template_2.pdf", "rb")
viewer = SimplePDFViewer(fd)
viewer.render()
markdown = viewer.canvas.strings
print(markdown)

class InvoiceData:
    def __init__(self, invoice_number, date, amount, total):
        self.invoice_number = invoice_number
        self.date = date
        self.amount = amount
        self.total = total


def extract_invoice_number(input_list):
    extracted_data = []
    pattern = re.compile(r"INV-\d{4}")
    for item in input_list:
        if pattern.search(item):
            print(input_list.index(item))
            extracted_data.append(item)
    return extracted_data

inv_number = extract_invoice_number(markdown)
print(inv_number)

def extract_table(input_list,):
    extracted_table = []




