import re
import pdfplumber
import pandas as pd

def clean_cell(cell):
    if not cell:
        return ""
    return re.sub(r"\s+", " ", cell).strip()

def parse_pdf_dict(path):
    variables = []
    current_header = None
    
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    row = [clean_cell(c) for c in row]
                    
                    if row[:3] == ["Descrição", "Código", "Tipo de Dado"]:
                        current_header = row
                        continue
                    
                    if not current_header:
                        continue

                    if len([c for c in row if c]) < 3:
                        continue

                    if len(row) < len(current_header):
                        row += [""] * (len(current_header) - len(row))
                    
                    var = {
                        "descricao": row[0],
                        "codigo": row[1],
                        "tipo": row[2],
                        "formato": row[3],
                        "permite_nulo": row[4],
                        "permite_zerado": row[5],
                        "permite_negativo": row[6] if len(row) > 6 else ""
                    }
                    
                    variables.append(var)
    
    return pd.DataFrame(variables)

df = parse_pdf_dict("base/dicionario_reservatorio.pdf")

print(df)