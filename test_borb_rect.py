import _conf as cfg

#!chapter_002/src/snippet_020.py
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.pdf.canvas.color.color import HexColor

from decimal import Decimal


def main():
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)


    """
    A4 — формат бумаги, определённый стандартом ISO 216, основан на
    метрической системе мер. Его размеры — 210×297 мм, диагональ — 364 мм.
    Площадь листа формата A4 приблизительно = 1/16 м².
    
    297 * 2 = 594
    210 * 4 = 840
    """


    # define layout rectangle
    # fmt: off
    r: Rectangle = Rectangle(       # 848 х 595  L (0,0)
        Decimal(10+1),                # x: лівий край + отступ
        Decimal(10+1),                # y: нижній край page_height - page_margin - height_of_textbox
        Decimal(594 - 10 * 2),      # width: правий край - два отступа 
        Decimal(840 - 10 * 2),      # height верхній край
    )
    # fmt: on

    # this is a quick hack to easily get a rectangle on the page
    # which can be very useful for debugging

    page.add_annotation(SquareAnnotation(r, stroke_color=HexColor("#ff0000")))

    # the next line of code uses absolute positioning
    # Paragraph("Hello World!", horizontal_alignment=Alignment.CENTERED).layout(page, r)
    r.add(Paragraph("Hello World!", horizontal_alignment=Alignment.CENTERED))

   # layout.add(
   #  	Paragraph("Державна служба України з надзвичайних ситуацій",
  

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()