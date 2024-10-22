#going to test gmft to extract tables from FINRA documents

import importlib
import gmft
import gmft.table_detection
import gmft.table_visualization
import gmft.table_function
import gmft.table_function_algorithm
import gmft.table_captioning
import gmft.pdf_bindings.bindings_pdfium
import gmft.pdf_bindings
import gmft.common

importlib.reload(gmft)
importlib.reload(gmft.common)
importlib.reload(gmft.table_captioning)
importlib.reload(gmft.table_detection)
importlib.reload(gmft.table_visualization)
importlib.reload(gmft.table_function)
importlib.reload(gmft.table_function_algorithm)
importlib.reload(gmft.pdf_bindings.bindings_pdfium)
importlib.reload(gmft.pdf_bindings)

from gmft.pdf_bindings import PyPDFium2Document
from gmft.auto import CroppedTable, AutoTableDetector
from gmft.auto import AutoTableFormatter

detector = AutoTableDetector()
formatter = AutoTableFormatter()

def ingest_pdf(pdf_path) -> list[CroppedTable]:
    doc = PyPDFium2Document(pdf_path)

    tables = []
    for page in doc:
        tables += detector.extract(page)
    return tables, doc

tables, doc = ingest_pdf('finra2.pdf')

for table in tables:
    ft = formatter.extract(table)
    #send the dataframe to the appropriate place in db
    print(ft.df())
    #might be a good idea to save the text representation too
    print (table.text())
    #here's the 'captions' which means title, subtitle, and any captions
    print (table.captions())

