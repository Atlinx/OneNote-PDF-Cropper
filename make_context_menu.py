import os
import sys
from context_menu import menus
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict

def exec_menu_command(file_names, params):
  for file_name in file_names:
    if file_name.endswith('.pdf'):
      input1 = PdfReader(file_name)
      output = PdfWriter(f"{os.path.splitext(file_name)[0]}_cropped.pdf")

      for page in input1.pages[1:]:
        position = (72, 160)
        dimensions = (8.5, 11.0)
        pixel_height = 596
        pixel_dim = (pixel_height * dimensions[0] / dimensions[1], pixel_height)
        
        info = PageMerge().add(page)
        x1, y1, x2, y2 = info.xobj_box
        viewrect = (
          position[0],
          position[1],
          position[0] + pixel_dim[0],
          position[1] + pixel_dim[1]
        )
        page = PageMerge().add(page, viewrect=info.xobj_box)
        page.resources
        page.cbox = viewrect
        page[0].scale(1.4)

        output.addpage(page.render())

      # finally, write "output" to document-output.pdf
      output.write()
  
if __name__ == '__main__':
  fc = menus.FastCommand('Crop OneNote PDF', type='FILES', python=exec_menu_command)
  fc.compile()