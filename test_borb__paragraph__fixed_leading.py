from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import PDF

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

    # add a Paragraph
    layout.add(Paragraph('NO fixed_leading: ' + LOREM_IPSUM))
    layout.add(Paragraph('fixed_leading=Decimal(1): ' + LOREM_IPSUM, fixed_leading=Decimal(1)))
    layout.add(Paragraph('fixed_leading=Decimal(10): ' + LOREM_IPSUM, fixed_leading=Decimal(10)))
    layout.add(Paragraph('fixed_leading=Decimal(20): ' + LOREM_IPSUM, fixed_leading=Decimal(20)))

    # store
    with open("borb__paragraph__fixed_leading.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()