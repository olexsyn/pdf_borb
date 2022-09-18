import _conf as cfg

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import Paragraph
#from borb.pdf.canvas.geometry.rectangle import Rectangle
#from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout  # SingleColumnLayout
from borb.pdf import MultiColumnLayout
from borb.pdf import PageLayout
from borb.pdf.canvas.layout.layout_element import LayoutElement
# from borb.pdf import ChunkOfText
# from borb.pdf.canvas.layout.list.ordered_list import OrderedList
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType
# from borb.pdf.canvas.layout.list.ordered_list import OrderedList
from borb.pdf import FixedColumnWidthTable
from borb.pdf import TableCell
# from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont  # custom_font
from borb.pdf import HexColor, X11Color
from borb.pdf import PDF
from borb.pdf import Barcode, BarcodeType
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf import Alignment
from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation


from decimal import Decimal
from pathlib import Path  # font_path


cer_id         = 772                            # номер сертифіката (свідоцтва)
cer_pref       = '99-04-32'                     # префікс сертифіката (свідоцтва)
cer_dt         = "15.09.2022 р."
equip_sn       = '1888'                         # серійний номер обладнання
equip_name     = "Анемометр"
equip_type     = "МС-13"
region_name    = "Дніпропетровський РЦГМ"
station_name   = "ЛСЗА Кам’янське"
manager_name   = "Інна АЛЕКСЄЄНКО"              # керівник/менеджер
assistent_name = "Володимир ІСАЄВ"
atm_temp       = '99.90'
atm_humd       = '65'
atm_pres       = '992.5'

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


    # r: Rectangle = Rectangle(       # 848 х 595  L (0,0)
    #     Decimal(10+1),                # x: лівий край + отступ
    #     Decimal(10+1),                # y: нижній край page_height - page_margin - height_of_textbox
    #     Decimal(594 - 10 * 2),      # width: правий край - два отступа 
    #     Decimal(840 - 10 * 2),      # height верхній край
    # )

    
    # construct the Font object
    #font_path: Path = Path("/usr/share/fonts/truetype/litefonts/Roboto-Regular.ttf")
    # font_path: Path = Path(__file__).parent / "Helvetica_Cyrillic.ttf"
    #font_path: Path = Path(__file__).parent / "Roboto-Regular.ttf"
    font_path: Path = Path("/usr/share/fonts/truetype/litefonts/Roboto-Regular.ttf")
    font_RobotoRegular: Font = TrueTypeFont.true_type_font_from_file(font_path)
    font_path: Path = Path("/usr/share/fonts/truetype/litefonts/Roboto-Bold.ttf")
    font_RobotoBold: Font = TrueTypeFont.true_type_font_from_file(font_path)


    """
    A4 — формат паперу, визначений стандартом ISO 216, ґрунтується на метричній
    системі заходів. Його розміри – 210×297 мм, діагональ – 364 мм.
    Площа аркуша формату A4 приблизно = 1/16 м².

    297 * 2 = 594
    210 * 4 = 840

    Про відступи
    Можливо, заплутано, але a Page не має полів. А Page — це просто чисте полотно,
    на якому речі можна малювати або відтворювати. A PageLayout вирішує, де кожен
    LayoutElement (наприклад, Paragraph) закінчиться. Тому вам потрібно подивитися
    там, якщо ви хочете встановити поля.
    Коли я дивлюся MultiColumnLayout, наприклад, його конструктор приймає атрибут
    horizontal_margin і vertical_margin

    """

    # meteo_logo: Image(
    #                     Path("/home/olex/www/meteo/meteo.pp.ua/img/logo_meteo.png"),
    #                     width=Decimal(100),
    #                     height=Decimal(100),
    #                 )

    rect: Rectangle = Rectangle(
        Decimal(60), Decimal(125), Decimal(250), Decimal(100),
        #            вісь Y,                   зсув по Y висота
        # вісь Х,                 зсув по X ширина 
    )

    stamp: Image = Image(
        Path("/home/olex/www/meteo/meteo.pp.ua/img/__stamp_meteo_4_pdf.png"),
        width=Decimal(120),
        height=Decimal(120),
    )

    stamp.paint(page, rect)

    layout.add(
            FixedColumnWidthTable(
                number_of_columns=3,
                number_of_rows=4,
                # adjust the ratios of column widths for this FixedColumnWidthTable
                column_widths=[Decimal(1), Decimal(6), Decimal(1)],
            )
            .add(
                TableCell(
                    Image(
                        Path("/home/olex/www/meteo/meteo.pp.ua/img/logo_meteo_4_pdf.png"),
                        width=Decimal(50),
                        height=Decimal(75),
                    ), #border_top=False,border_left=False,border_right=False,border_bottom=False, 
                    row_span=4 ,
                    padding_left=Decimal(15),
                    # /work/www/meteo/meteo.pp.ua/img/__stamp_meteo_4_pdf.png
                )
            )
            .add(
                Paragraph("Державна служба України з надзвичайних ситуацій",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                    font_size=Decimal(12),
                    font_color=HexColor("333333"),
                    padding_bottom=Decimal(12),
                ),
            )
            .add(
                TableCell(
                    Image(
                        Path("/home/olex/www/meteo/meteo.pp.ua/img/logo_dsns.jpg"),
                        width=Decimal(70),
                        height=Decimal(70),
                    ),
                    row_span=4,
                )
            )
            .add(
                Paragraph("УКРАЇНСЬКИЙ ГІДРОМЕТЕОРОЛОГІЧНИЙ ЦЕНТР",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoBold,
                    font_size=Decimal(15), # font_color=HexColor("333333")
                    font_color=X11Color("DarkBlue"),
                    padding_bottom=Decimal(4),
                )
            )
            .add(
                Paragraph("Головний центр технічного обслуговування засобів вимірювання",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                    padding_bottom=Decimal(4),
                    # font_size=Decimal(11),
                )
            )
            .add(
                Paragraph("Відділ метрологічного забезпечення",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                )
            )
            .no_borders()
    )

    #layout.add(
    #    Paragraph("_" * 100,
    #       horizontal_alignment=Alignment.CENTERED,
    #       font=font_RobotoRegular,
    #       font_size=Decimal(8),
    #       padding_bottom=Decimal(4),
    #    )
    #)

    layout.add(
        Paragraph("СВІДОЦТВО ПРО КАЛІБРУВАННЯ",
           horizontal_alignment=Alignment.CENTERED,
           font=font_RobotoBold,
           font_size=Decimal(16),
        )
    )

    bar_code: Barcode = Barcode(
        f"{cer_pref}/{cer_id}",
        width=Decimal(210),
        height=Decimal(60),
        type=BarcodeType.CODE_128,
    )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=3,
            number_of_rows=1,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(4), Decimal(5), Decimal(3)],
        )
        .add(
            TableCell(
                Paragraph("Реєстраційний №",
                    #horizontal_alignment=Alignment.LEFT,
                    #vertical_alignment=Alignment.MIDDLE,
                    font=font_RobotoRegular,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(15),
                padding_left=Decimal(40),
            )
        )
        .add(
            bar_code
        )
        .add(
            TableCell(
                Paragraph(f"{cer_pref}/{cer_id}",
                    #vertical_alignment=Alignment.MIDDLE,
                    #horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(15),
                padding_left=Decimal(0),
            )
        )
        .no_borders()
    )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=2,
            number_of_rows=7,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(5), Decimal(4)],
        )
        .add(
            TableCell(
                Paragraph("Дата калібрування:",
                    #horizontal_alignment=Alignment.LEFT,
                    font=font_RobotoRegular,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(0),
            )
        )
        .add(
            TableCell(
                Paragraph(f"{cer_dt}",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(0),

            )
        )
        .add(
            Paragraph("Об’єкт калібрування:",
                #horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph(f"{equip_name}",
                horizontal_alignment=Alignment.CENTERED,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph("Тип:",
                #horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph(f"{equip_type}",
                horizontal_alignment=Alignment.CENTERED,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph("Заводський / серійний номер:",
                #horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph(f"{equip_sn}",
                horizontal_alignment=Alignment.CENTERED,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph("Замовник:",
                horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph(f"{region_name}\n\n{station_name}",
                font=font_RobotoRegular,
                horizontal_alignment=Alignment.CENTERED,
                respect_newlines_in_text=True,
            ),
        )
        .add(
            Paragraph("Місце проведення калібрування:",
                #horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph("Відділ метрологічного\nзабезпечення\nм. Київ, проспект Науки, 37",
                horizontal_alignment=Alignment.CENTERED,
                font=font_RobotoRegular,
                respect_newlines_in_text=True,
                respect_spaces_in_text=True,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph("Кількість сторінок свідоцтва:",
                horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            Paragraph("2",
                horizontal_alignment=Alignment.CENTERED,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .set_padding_on_all_cells(Decimal(16), Decimal(0), Decimal(16), Decimal(40))
        .no_borders()
        # .even_odd_row_colors(X11Color("LightGray"), X11Color("White"))
    )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=3,
            number_of_rows=2,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(4), Decimal(3), Decimal(3)],
        )
        .add(
            TableCell(
            Paragraph("Начальник відділу",
                horizontal_alignment=Alignment.RIGHT,
                #vertical_alignment=Alignment.MIDDLE,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            ),
            padding_top=Decimal(25),
            padding_left=Decimal(40),
            )
        )
        .add(
            TableCell(
            Paragraph("_" * 18),
            padding_top=Decimal(25),
            padding_left=Decimal(30),
            )
        )
        .add(
            TableCell(
            Paragraph(manager_name,
                #vertical_alignment=Alignment.MIDDLE,
                #horizontal_alignment=Alignment.CENTERED,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            ),
            padding_top=Decimal(25),
            padding_left=Decimal(22),
            )
        )
        .add(
            TableCell(
                Paragraph("")
            )
        )
        .add(
            TableCell(
                Paragraph("Підпис",
                    font=font_RobotoRegular,
                    font_size=Decimal(8), 
                ),
                padding_top=Decimal(0),
                padding_left=Decimal(70),
            )
        )
        .add(
            TableCell(
                Paragraph("Прізвище, ініціали",
                    font=font_RobotoRegular,
                    font_size=Decimal(8), 
                ),
                padding_top=Decimal(5),
                padding_left=Decimal(50),
            )
        )
        .no_borders()
    )

    qr_code: Barcode = Barcode(
        f"https://meteo.pp.ua/docs/sert/{cer_pref}/{cer_id}",
        width=Decimal(110),
        height=Decimal(110),
        type=BarcodeType.QR,
        horizontal_alignment=Alignment.RIGHT,
    )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=2,
            number_of_rows=1,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(5), Decimal(3)],
        )
        .add(
            TableCell(
                Paragraph("""
Адреса: пр-т. Науки 37, м.Київ, 03028, Україна
Телефон: +3(044)525-69-63, +3(044)525-95-12
Електронна адреса: vmz@meteo.gov.ua, gcto@meteo.gov.ua""",
                    horizontal_alignment=Alignment.LEFT,
                    font=font_RobotoRegular,
                    respect_newlines_in_text=True,
                    respect_spaces_in_text=True,
                    font_size=Decimal(10),
                    padding_top=Decimal(30),
                    padding_left=Decimal(40),
                    #border_bottom=False,
                    #border_left=False,
                    #border_right=False,
                    #border_top=False,
                ),
            )
        )
        .add(
            TableCell(
                    qr_code,
                    padding_top=Decimal(0),
                    padding_left=Decimal(0),
                ),
        )
        #.set_padding_on_all_cells(Decimal(40), Decimal(0), Decimal(0), Decimal(40))
        .no_borders()
    )


# ----------------------------------------------------------

    # create new Page
    page: Page = Page()

    doc.add_page(page)

    # set a PageLayout
    # layout: PageLayout = SingleColumnLayout(page)
    layout: PageLayout = MultiColumnLayout(page,
        number_of_columns = 1,
        horizontal_margin = Decimal(40),
        vertical_margin = Decimal(40),
    )

    layout.add(
            FixedColumnWidthTable(
                number_of_columns=1,
                number_of_rows=4,
            )
            .add(
                Paragraph("Державна служба України з надзвичайних ситуацій",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                ),
            )
            .add(
                Paragraph("УКРАЇНСЬКИЙ ГІДРОМЕТЕОРОЛОГІЧНИЙ ЦЕНТР",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                )
            )
            .add(
                Paragraph("Головний центр технічного обслуговування засобів вимірювання",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                )
            )
            .add(
                Paragraph("Відділ метрологічного забезпечення",
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                )
            )
            .no_borders()
    )

    # layout.add(
    #     Paragraph("СВІДОЦТВО ПРО КАЛІБРУВАННЯ",
    #        horizontal_alignment=Alignment.CENTERED,
    #        font=font_RobotoBold,
    #        font_size=Decimal(16),
    #     )
    # )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=3,
            number_of_rows=3,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(6), Decimal(4), Decimal(4)],
        )
        .add(Paragraph(""),
        )
        .add(Paragraph(""),
        )
        .add(
            TableCell(
                Paragraph("Сторінка 2",
                    horizontal_alignment=Alignment.RIGHT,
                    font=font_RobotoRegular,
                ),
                padding_top=Decimal(10),
            )
        )
        .add(
            TableCell(
                Paragraph("Свідоцтво про калібрування",
                    horizontal_alignment=Alignment.LEFT,
                    #vertical_alignment=Alignment.MIDDLE,
                    font=font_RobotoBold,
                    # padding_top=Decimal(3),
                    font_size=Decimal(14), 
                ),
                padding_top=Decimal(15),
                #padding_left=Decimal(40),
            )
        )
        .add(
            TableCell(
                Paragraph("Реєстраційний №",
                    #horizontal_alignment=Alignment.LEFT,
                    #vertical_alignment=Alignment.MIDDLE,
                    font=font_RobotoBold,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(15),
                padding_left=Decimal(40),
            )
        )
        .add(
            TableCell(
                Paragraph(f"{cer_pref}/{cer_id}",
                    #horizontal_alignment=Alignment.LEFT,
                    #vertical_alignment=Alignment.MIDDLE,
                    font=font_RobotoBold,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(15),
                padding_left=Decimal(10),
            )
        )
        .add(
            TableCell(
                Paragraph("Серійний номер ЗВТ:",
                    #vertical_alignment=Alignment.MIDDLE,
                    horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(15),
                padding_left=Decimal(0),
            )
        )
        .add(
            TableCell(
                Paragraph(equip_sn,
                    #vertical_alignment=Alignment.MIDDLE,
                    #horizontal_alignment=Alignment.CENTERED,
                    font=font_RobotoRegular,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                padding_top=Decimal(15),
                padding_left=Decimal(0),
            )
        )
        .add(
            TableCell(
                Paragraph("")
            )
        )
        .no_borders()
    )

    layout.add(
        FixedColumnWidthTable(
            number_of_columns=2,
            number_of_rows=6,
            # adjust the ratios of column widths for this FixedColumnWidthTable
            column_widths=[Decimal(4), Decimal(6)],
        )
        .add(
            TableCell(
                Paragraph("Метод калібрування",
                    #horizontal_alignment=Alignment.LEFT,
                    font=font_RobotoBold,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                #padding_top=Decimal(0),
                col_span=2,
            )
        )
        .add(
            Paragraph("")
        )
        .add(
            Paragraph("Метод прямих багаторазових вимірювань, звірення з еталоном. «Анемометри чашечні ручні МС-13. Методика калібрування»",
                horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            TableCell(
                Paragraph("Умови проведення калібрування",
                    #horizontal_alignment=Alignment.LEFT,
                    font=font_RobotoBold,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                #padding_top=Decimal(0),
                col_span=2,
            )
        )
        .add(
            Paragraph("")
        )
        .add(
            Paragraph(f"температура {atm_temp} °С\nвідносна вологість повітря {atm_humd} %\nатмосферний тиск {atm_pres} кПа",
                horizontal_alignment=Alignment.LEFT,
                font=font_RobotoRegular,
                respect_newlines_in_text=True,
                respect_spaces_in_text=True,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .add(
            TableCell(
	            Paragraph("Калібрування проведено за допомогою",
                    #horizontal_alignment=Alignment.LEFT,
                    font=font_RobotoBold,
                    # padding_top=Decimal(3),
                    # font_size=Decimal(12), 
                ),
                #padding_top=Decimal(0),
                col_span=2,
            )
        )
        .add(
            Paragraph("")
        )
        .add(
            Paragraph("Еталон",
                horizontal_alignment=Alignment.LEFT,
                font=font_RobotoBold,
                # padding_top=Decimal(3),
                # font_size=Decimal(12), 
            )
        )
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        #.no_borders()
        # .even_odd_row_colors(X11Color("LightGray"), X11Color("White"))
    )

    # store
    with open("certificate.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
