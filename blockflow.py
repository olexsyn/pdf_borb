#!chapter_002/src/snippet_036.py
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf import ChunkOfText
from borb.pdf import BlockFlow
from borb.pdf import InlineFlow
from borb.pdf import HexColor

from decimal import Decimal

def main():

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    block: BlockFlow = BlockFlow()
    flow: InlineFlow = InlineFlow()
    # add a chunks
    flow.add(ChunkOfText("Hello", font="Helvetica"))
    flow.add(ChunkOfText("bold text", font="Helvetica-bold"))
    flow.add(ChunkOfText("!"))

    block.add(flow).add(Paragraph("\n", font_size=Decimal(0)))

    flow: InlineFlow = InlineFlow()
    # add a chunks
    flow.add(ChunkOfText("Hello again", font="Helvetica"))
    flow.add(ChunkOfText("italic text", font="Helvetica-oblique"))
    flow.add(ChunkOfText("!!!"))

    block.add(flow).add(Paragraph("\n", font_size=Decimal(0)))

    flow: InlineFlow = InlineFlow()
    # add a chunks
    flow.add(ChunkOfText("Hello again", font="Helvetica"))
    flow.add(ChunkOfText("italic text", font="Helvetica-oblique"))
    flow.add(ChunkOfText("!!!"))

    block.add(flow)


        



    ## block aggregates other LayoutElements
    #block.add(
    #        flow
    #    #).add(
    #    #    #Paragraph("next line here\n", respect_newlines_in_text=True)
    #    #    Paragraph("\n")
    #    ).add(
    #        flow2
    #    )

    layout.add(block)

    # store
    with open("__pdf/blockflow.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()