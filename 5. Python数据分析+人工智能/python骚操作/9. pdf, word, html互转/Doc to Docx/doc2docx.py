from win32com import client


def doc2docx(doc_name, docx_name):
    try:
        word = client.DispatchEx('Word.Application')
        doc = word.Documents.Open(doc_name)
        doc.SaveAs(docx_name, 16)
        doc.Close()
        word.Quit()
    except:
        pass


if __name__ == '__main__':
    doc2docx('letter.doc', 'result.docx')
