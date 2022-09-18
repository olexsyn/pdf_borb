from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.lipsum.lipsum import Lipsum

from decimal import Decimal

LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
    fugiat nulla pariatur."""

def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add a Paragraphs
    layout.add(Paragraph('NO multiplied_leading: ' + LOREM_IPSUM))
    layout.add(Paragraph('multiplied_leading=Decimal(1): ' + LOREM_IPSUM, multiplied_leading=Decimal(1)))
    layout.add(Paragraph('multiplied_leading=Decimal(2): ' + LOREM_IPSUM, multiplied_leading=Decimal(2)))
    layout.add(Paragraph('multiplied_leading=Decimal(3): ' + LOREM_IPSUM, multiplied_leading=Decimal(3)))

    # store
    with open("borb__paragraph__multiplied_leading.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()