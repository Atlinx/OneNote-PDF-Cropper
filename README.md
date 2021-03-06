# ✂ iPad OneNote PDF Cropper 📄

A tool that removes the margins from 8.5 x 11 inch PDFs exported from OneNote. It's available as a right-click menu option when you right click a file. This works with Mac, Linux, and Windows.

## Important Notes

The PDF must be exported using **Microsft Print to PDF**, **Adobe PDF**, or any other **exporter that creates pages**. The resulting PDF should be centered horizontally and vertically aligned to the top.
 
This cropper **does NOT work with PDFs exported by iOS**, because iOS will export a large single page PDF.
 
The PDF must've been **inserted into the OneNote on the iPad**, because otherwise the size of each pdf page will be different. PDFs inserted on windows desktop are larger than PDFs inserted on the ipad, which screws up the cropping. (Curse you OneNote for your inconsistent design!!! 😠).

Oh the lengths we have to go to for janky technology... 😞

## Installation

> **NOTE**
> 
> This requires [python3](https://www.python.org/downloads/) or greater.

1. Clone/download the repository

2. Install the requirements by going to the repository's folder and running,

```bash
> pip install -r requirements.txt
```

3. Run `make_context_menu.py` 
```bash
> python make_context_menu.py
```

4. **Voila!** You should be able to right click a file and click the menu option `Crop OneNote PDF`.

## Usage

1. Select one or more PDF files that are exported from OneNote (the PDF files msut meet the requirements mentioned in [important-notes](#important-notes)). 

2. Right click them to bring up a context menu, and then select `Crop OneNote PDF` to crop the selected pdfs.

3. The cropped pdfs will be placed in the same folder as the original pdfs.
