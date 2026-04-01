import pypdf
import sys

template = pypdf.PdfReader(open('super.pdf', 'rb'))
watermark = pypdf.PdfReader(open('wtr.pdf', 'rb'))
output = pypdf.PdfWriter()

for page in template.pages:
    page.merge_page(watermark.pages[0], over=False)
    output.add_page(page)

    with open('watermarked.pdf', 'wb') as f:
        output.write(f)

