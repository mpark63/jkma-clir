from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document

def main():
    ## create document for extraction with configurations
    pdf_document = Document(
        document_path='<REPLACE_WITH_YOUR_PDF_PATH>',
        language='kor'
        )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    print(content)

if __name__ == "__main__":
    main()
