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
        merger.append(pdf)

    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    merger.close()
    print(f"PDFs merged successfully into {output_filename}")

if __name__ == "__main__":
    # Example usage:
    # Create some dummy PDF files for demonstration if they don't exist
    # (In a real scenario, these would be your actual PDF files)
    # You can use a tool or library to create simple PDFs if needed for testing.

    # Assuming 'file1.pdf', 'file2.pdf', 'file3.pdf' exist in the same directory
    # Replace these with your actual PDF file paths
    pdf_files_to_merge = ["file1.pdf", "file2.pdf", "file3.pdf"]
    output_merged_pdf = "merged_document.pdf"

    merge_pdfs(pdf_files_to_merge, output_merged_pdf)
