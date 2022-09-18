#!chapter_005/src/snippet_027.py
import typing
from borb.pdf import Document
from borb.pdf import PDF

import typing

from borb.pdf import HexColor
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import Alignment
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF


def main():

    d: Document = Document()
    p: Page = Page()
    d.add_page(p)

    l: PageLayout = SingleColumnLayout(p)
    l.add(
        Paragraph(
            """
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                    """,
            font_color=HexColor("de6449"),
            text_alignment=Alignment.JUSTIFIED,
        )
    )

    with open("__pdf/test_borb_005sn027.pdf", "wb") as pdf_out_handle:
        PDF.dumps(pdf_out_handle, d)


if __name__ == "__main__":
    main()