from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf.canvas.layout.text.codeblock import CodeBlock
from borb.pdf import PDF

def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    layout.add(
        Paragraph("Test")
    ).add(
        CodeBlock("""
def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    # layout: PageLayout = SingleColumnLayout(page)
    layout: PageLayout = MultiColumnLayout(page,
        number_of_columns = 1,
        horizontal_margin = Decimal(40),
        vertical_margin = Decimal(40),
    )""",
            border_top = True,
            border_right = True,
            border_bottom = True,
            border_left = True,
        )
    ).add(
        Paragraph("Test Test Test Test")
    )

    # store
    with open("__pdf/codeblock.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
