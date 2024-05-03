# importing required modules 
from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document

def main():
    ## create document for extraction with configurations
    pdf_document = Document(
        document_path='/Users/mpark/Desktop/full/0a13ada333f539ed53ed3c3789459bf82f0d39ac.pdf',
        language='kor'
        )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    print(content)

if __name__ == "__main__":
    main()
