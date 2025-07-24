import os
import csv
from PyPDF2 import PdfMerger

def merge_pdfs(input_pdfs, output_filename):
    """
    Merges multiple PDF files into a single output PDF.

    Args:
        input_pdfs (list): A list of paths to the input PDF files.
        output_filename (str): The name of the output merged PDF file.
    """
    merger = PdfMerger()

    for pdf in input_pdfs:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"ERROR: can't find {pdf}")

    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    merger.close()
    print(f"PDFs merged successfully into {output_filename}")

if __name__ == "__main__":
    with open('files.csv', mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row
        print(f"Header: {header}")
        for row in csv_reader:
            output_name = row[0]
            input_names = list(filter(None, row[1:]))
            print(f"Input: {input_names}")
            print(f"Output: {output_name}")
            merge_pdfs(input_names, output_name)
