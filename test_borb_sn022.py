import _conf as cfg

#!chapter_005/src/snippet_035.py
import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF

import typing
from decimal import Decimal

from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.page_layout.multi_column_layout import MultiColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.color.color import HexColor


def main():

    # create new document
    d: Document = Document()

    # add Page
    p: Page = Page()
    d.add_page(p)
    page_number: int = 1

    # create PageLayout
    l: PageLayout = MultiColumnLayout(p)

    # adding Pages
    for _ in range(0, 20):
        if l.get_page() != p or page_number == 1:
            l.add(
                Paragraph(
                    "Page %d" % page_number,
                    font_color=HexColor("f1cd2e"),
                    font_size=Decimal(20),
                    font="Courier-Bold",
                )
            )
            p = l.get_page()
            page_number += 1

        l.add(
            Paragraph(
                """
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        """
            )
        )

    # write
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, d)


if __name__ == "__main__":
    main()
