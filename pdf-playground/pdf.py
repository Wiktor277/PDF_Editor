import pypdf
import sys

input = sys.argv[1:]

def pdf_combiner(pdf_files):
    pdf_writer = pypdf.PdfWriter()
    for pdf_file in pdf_files:
        pdf_reader = pypdf.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open('Super.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)

pdf_combiner(input)



# with open("dummy.pdf", 'rb') as file:
#     reader = pypdf.PdfReader(file)
#     page = reader.pages[0]
#     page.rotate(-90)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer = pypdf.PdfWriter()
#         writer.add_page(page)
#         writer.write(new_file)

# pdf_writer = pypdf.PdfWriter()
#     for pdf_file in pdf_files:
#         pdf_reader = pypdf.PdfReader(pdf_file)
#         for page in pdf_reader.pages:
#             pdf_writer.add_page(page)
#     with open('output.pdf', 'wb') as output_file:
#         pdf_writer.write(output_file)




