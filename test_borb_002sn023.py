import _conf as cfg

#!chapter_002/src/snippet_023.py
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf import Alignment
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.pdf import HexColor
from borb.pdf import Barcode, BarcodeType

from decimal import Decimal


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # define layout rectangle
    # fmt: off
    r: Rectangle = Rectangle(
        Decimal(59),                # x: 0 + page_margin
        Decimal(848 - 84 - 200),    # y: page_height - page_margin - height_of_textbox
        Decimal(595 - 59 * 2),      # width: page_width - 2 * page_margin
        Decimal(200),               # height
    )
    # fmt: on

    r2: Rectangle = Rectangle(
        Decimal(40), Decimal(40), Decimal(250), Decimal(100),
        #            вісь Y,                   зсув по Y висота
        # вісь Х,                 зсув по X ширина 
    )

    bar_code: Barcode = Barcode(
        "99-04-32/712",
        width=Decimal(250),
        height=Decimal(50),
        type=BarcodeType.CODE_128,
    )
    qr_code: Barcode = Barcode(
        "https://meteo.pp.ua/doc/99-04-32/712",
        width=Decimal(128),
        height=Decimal(128),
        type=BarcodeType.QR,
    )


    # this is a quick hack to easily get a rectangle on the page
    # which can be very useful for debugging
    page.add_annotation(SquareAnnotation(r, stroke_color=HexColor("#ff0000")))
    page.add_annotation(SquareAnnotation(r2, stroke_color=HexColor("#00ff00")))

    # the next line of code uses absolute positioning
    qr_code.paint(page, r)
    bar_code.paint(page, r2)

    # Paragraph("World Hello!",
    #     vertical_alignment=Alignment.MIDDLE,
    #     horizontal_alignment=Alignment.CENTERED,
    # b_code).paint(page, r2)

    #layout.add(
    #    Barcode(
    #        "1234567896120",
    #        width=Decimal(128),
    #        height=Decimal(128),
    #        type=BarcodeType.EAN_14,
    #    )
    #)


    # store
    with open("__pdf/output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
    