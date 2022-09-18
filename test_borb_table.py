import _conf as cfg

#!chapter_003/src/snippet_009.py

from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import FixedColumnWidthTable
from borb.pdf import TableCell
from borb.pdf import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf import OrderedList
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PDF
# from borb.pdf import ChunkOfText
# from borb.pdf import InlineFlow
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont

from decimal import Decimal
from pathlib import Path

def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # list: OrderedList = (
    #         OrderedList()
    #         .add(Paragraph("Item 1"))
    #         .add(Paragraph("Item 2"))
    #         .add(Paragraph("Item 4"))
    # )

    # flow: InlineFlow = InlineFlow()


    font_path: Path = Path("/usr/share/fonts/truetype/litefonts/Roboto-Regular.ttf")
    font_RobotoRegular: Font = TrueTypeFont.true_type_font_from_file(font_path)


    # add a Paragraph

    # flow.add(
    #     Paragraph("Відділ метрологічного забезпечення м. Київ, проспект Науки, 37",
    #         # respect_newlines_in_text=True,
    #         # respect_spaces_in_text=True,
    #         font=font_RobotoRegular,
    #     )
    # )

    """
    Відділ метрологічного\n
    забезпечення\n
    м. Київ, проспект Науки, 37
    """


    #flow.add(Paragraph("Hello"))
    #flow.add(Paragraph(", bobr"))
    #flow.add(Paragraph("!"))

    #list: OrderedList = (
    #        OrderedList()
    #        .add(Paragraph("Item 1"))
    #        .add(Paragraph("Item 2"))
    #        .add(Paragraph("Item 4"))
    #)

    # create a FixedColumnWidthTable
    layout.add(
        FixedColumnWidthTable(number_of_columns=2, number_of_rows=2,column_widths=[Decimal(1), Decimal(4)])
        .add(Paragraph("Lorem"))
        .add(Paragraph("Ipsum",horizontal_alignment=Alignment.RIGHT,))
        .add(Paragraph("Dolor"))
        .add(Paragraph("Amet",horizontal_alignment=Alignment.RIGHT,))
        # set padding on all (implicit) TableCell objects in the FixedColumnWidthTable
        .set_padding_on_all_cells(Decimal(50), Decimal(10), Decimal(50), Decimal(10))
    )

    # store
    with open("borb_table.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()