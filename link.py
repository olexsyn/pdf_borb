#!chapter_002/src/snippet_036.py
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import ChunkOfText
from borb.pdf import HexColor
from borb.pdf import PDF
from borb.pdf.canvas.layout.emoji.emoji import Emojis
# from borb.pdf.canvas.layout.text.chunk_of_text import ChunkOfText
from borb.pdf.canvas.layout.annotation.remote_go_to_annotation import RemoteGoToAnnotation
from borb.pdf import InlineFlow

email = "olex@example.com"


def main():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)
    flow: InlineFlow = InlineFlow()

    link: ChunkOfText = ChunkOfText(email,
                            font="Helvetica-oblique",
                            font_color=HexColor("6495ED")
                            # font_color=HexColor("#6d64e8")
                        )
    # link: Paragraph = Paragraph("this is the link", font="Helvetica-bold")

    # add a Paragraph
    flow.add(ChunkOfText("Hello"))
    flow.add(link)
    flow.add(ChunkOfText("!"))
    layout.add(flow)

    page.add_annotation(
        RemoteGoToAnnotation(link.get_previous_paint_box(), uri=f"mailto:{email}")
    )

    with open("__pdf/link.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)


if __name__ == "__main__":
    main()

