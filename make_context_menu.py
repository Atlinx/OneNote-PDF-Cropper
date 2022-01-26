import os
import sys
from context_menu import menus
from PyPDF2 import PdfFileWriter, PdfFileReader

def exec_menu_command(file_names, params):
  print(f"Hello! I'm running from {os.path.dirname(file_names[0])} \n")
  print(f"Current right clicked file: {file_names}")

  for file_name in file_names:
    if file_name.endswith('.pdf'):
      with open(file_name, "rb") as inputstream:
        output = PdfFileWriter()
        input1 = PdfFileReader(inputstream)

        for page in input1.pages[1:]:
          position = (72, 160)
          dimensions = (8.5, 11.0)
          pixel_height = 596
          pixel_dim = (pixel_height * dimensions[0] / dimensions[1], pixel_height)
          width = page.mediaBox.upperRight[0]
          height = page.mediaBox.upperRight[1]

          page.mediaBox.upperRight = (
              position[0] + pixel_dim[0],
              position[1] + pixel_dim[1]
          )

          page.mediaBox.lowerLeft = (
              position[0],
              position[1]
          )
          
          output.addPage(page)

        # finally, write "output" to document-output.pdf
        with open(f"{os.path.splitext(file_name)[0]}_cropped.pdf", "wb") as output_stream:
          output.write(output_stream)
  
if __name__ == '__main__':
  fc = menus.FastCommand('Crop OneNote PDF', type='FILES', python=exec_menu_command)
  fc.compile()