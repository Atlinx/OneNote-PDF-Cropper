import os
import sys
from context_menu import menus
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.pdf import PageObject

def exec_menu_command(file_names, params):
  for file_name in file_names:
    if file_name.endswith('.pdf'):
      with open(file_name, "rb") as inputstream:
        output = PdfFileWriter()
        input1 = PdfFileReader(inputstream)

        og_height = 596
        target_size = (int(8.5*72), int(11*72))
        scale_factor = target_size[1] / og_height
        translation = (-72 * scale_factor, -161 * scale_factor)
          
        idx = 0
        for page in input1.pages[1:]:
          idx += 1
          print(f'Starting new page: {idx}')
          newPage = PageObject.createBlankPage(None, target_size[0], target_size[1])
          newPage.mergeScaledTranslatedPage(page, scale_factor, translation[0], translation[1])

          print(f'Adding new page: {idx}')
          output.addPage(newPage)

        # finally, write "output" to document-output.pdf
        with open(f"{os.path.splitext(file_name)[0]}_cropped.pdf", "wb") as output_stream:
          output.write(output_stream)
  
if __name__ == '__main__':
  fc = menus.FastCommand('Crop OneNote PDF', type='FILES', python=exec_menu_command)
  fc.compile()