import os
from win32com import client


def doc2pdf(doc_name, pdf_name):
    try:
        word = client.Dispatch('Word.Application')
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        worddoc = word.Documents.Open(doc_name, ReadOnly=1)
        worddoc.SaveAs(pdf_name, FileFormat=17)
        worddoc.Close()
        return pdf_name
    except:
        return 1


if __name__ == '__main__':
    doc_name = 'letter.doc'
    pdf_name = 'result.pdf'
    print(doc2pdf(doc_name, pdf_name))
