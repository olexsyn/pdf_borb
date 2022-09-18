from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import MultiColumnLayout
from borb.pdf import Paragraph
from borb.pdf import Alignment
from borb.pdf import FixedColumnWidthTable
from borb.pdf import TableCell
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont  # custom_font
from borb.pdf import PDF

from decimal import Decimal
from pathlib import Path  # font_path


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
    )

    MY_SYS_FONTS = "/usr/share/fonts/truetype/litefonts/"

    # construct the Font object
    font_path: Path = Path(MY_SYS_FONTS + "Roboto-Regular.ttf")
    font_RobotoRegular: Font = TrueTypeFont.true_type_font_from_file(font_path)
    font_path: Path = Path(MY_SYS_FONTS + "Roboto-Bold.ttf")
    font_RobotoBold: Font = TrueTypeFont.true_type_font_from_file(font_path)

    layout.add(
        Paragraph("Alignment.CENTERED короткий текст\nа, це його новий рядок...",
            text_alignment=Alignment.CENTERED,
            font=font_RobotoRegular,
            respect_newlines_in_text=True,
        )
    ).add(
        Paragraph("а це Alignment.CENTERED\n Це просто довгий текст Це просто довгий текст Це просто довгий текст Це просто довгий текст Це просто довгий текст Це просто довгий текст",
            text_alignment=Alignment.CENTERED,
            font=font_RobotoBold,
            respect_newlines_in_text=True,
            #respect_newlines_in_text=True,
            # font_size=Decimal(12),
            # font_color=HexColor("333333"),
            padding_bottom=Decimal(15),
        )
    ).add(
        Paragraph("Page не має полів. Це просто чисте полотно, на якому речі можна малювати або відтворювати. A PageLayout вирішує, де кожен LayoutElement (наприклад, Paragraph) закінчиться. Тому вам потрібно дивитися в той бік, якщо ви хочете встановити поля. Якщо подивимося на MultiColumnLayout, наприклад, то його конструктор приймає атрибут horizontal_margin і vertical_margin",
            text_alignment=Alignment.JUSTIFIED,
            font=font_RobotoRegular,
            #font_size=Decimal(15),
            # font_color=X11Color("DarkBlue"),
            padding_bottom=Decimal(4),
        )
    ).add(
        Paragraph("Alignment.RIGHT короткий текст",
            text_alignment=Alignment.RIGHT,
            font=font_RobotoRegular,
        )
    ).add(
        Paragraph("Alignment.RIGHT Це просто довгий текст Це просто довгий текст Це просто довгий текст Це просто довгий текст Це просто довгий текст Це просто довгий текст",
            text_alignment=Alignment.RIGHT,
            font=font_RobotoRegular,
        )
    )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=1,
            number_of_rows=2,
        )
        .add(
            TableCell(
                Paragraph("horizontal_alignment діє у комірці таблиці",
                    horizontal_alignment=Alignment.RIGHT,
                    font=font_RobotoRegular,
                )
            )
        )
        .add(
            TableCell(
                Paragraph("text_alignment у комірці таблиці не діє!",
                    text_alignment=Alignment.RIGHT,
                    font=font_RobotoRegular,
                )
            )
        )
    )

    # layout.add(
    #     Paragraph("default font_size: Page не має полів. Це просто чисте полотно, на якому речі можна малювати або відтворювати.",
    #         text_alignment=Alignment.CENTERED,
    #         font=font_RobotoRegular,
    #         # font_size=Decimal(12),
    #         # font_color=HexColor("333333"),
    #         padding_bottom=Decimal(12),
    #     )
    # ).add(
    #     Paragraph("A PageLayout вирішує, де кожен LayoutElement (наприклад, Paragraph) закінчиться. Тому вам потрібно дивитися в той бік, якщо ви хочете встановити поля.",
    #         text_alignment=Alignment.JUSTIFIED,
    #         font=font_RobotoBold,
    #         font_size=Decimal(15),
    #         # font_color=X11Color("DarkBlue"),
    #         padding_bottom=Decimal(4),
    #     )
    # ).add(
    #     Paragraph("Якщо подивимося на MultiColumnLayout, наприклад, то його конструктор приймає атрибут horizontal_margin і vertical_margin",
    #         text_alignment=Alignment.RIGHT,
    #         font=font_RobotoRegular,
    #         font_size=Decimal(18),
    #         padding_bottom=Decimal(4),
    #     )
    # )

    # store
    with open("__pdf/paragraphs_fonts.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
