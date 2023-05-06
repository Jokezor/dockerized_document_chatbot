import sys, fitz
from get_documents import get_documents

def pdf_to_text_file(fname, destinationfile):
    print(fname)
    doc = fitz.open(fname)  # open document

    out = open(destinationfile + ".txt", "wb")  # open text output

    for page in doc:  # iterate the document pages
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
        out.write(text)  # write text of page
        out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
    out.close()


for document in get_documents("../bad_pdfs/"):
    pdf_to_text_file(f'../bad_pdfs/{document}', f'../docs/{document}')
