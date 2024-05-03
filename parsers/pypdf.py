import sys
import os
from py_pdf_parser.loaders import load_file
from py_pdf_parser import tables

def parse(pdf_name, pdf_path): 
    # load the document
    document = load_file(pdf_path)

    # extract reference elements:
    print(document.elements)

    # remove tables
    # tabular_data = tables.extract_table(document.elements, fix_element_in_multiple_rows=True, fix_element_in_multiple_cols=True)
    
    # aggregate text 
    content_text = "\n".join(element.text() for element in document.elements)

    # Open a file in write mode ('w')
    with open(f'txt/{pdf_name}.txt', 'w') as file:
        # Write content to the file
        file.write(content_text)



def main(pdf_name, pdf_path):
    # Your main script logic here
    print("Processing PDF:", pdf_path)
    parse(pdf_name, pdf_path)
    # Example: You can use pdf_path to do something with the PDF file

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python your_script.py <pdf_file_path>")
        sys.exit(1)

    # Get the PDF file path from command line arguments
    pdf_name = sys.argv[1]
    pdf_path = sys.argv[2]

    # Check if the provided path is a valid file
    if not os.path.isfile(pdf_path):
        print("Error: Provided path is not a valid file.")
        sys.exit(1)

    # Call the main function with the PDF file path
    main(pdf_name, pdf_path)
