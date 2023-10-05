# MD2PDF

MD2PDF is a CLI Tool created with Python 3 that allows you to convert your markdown documents into pdfs. There are several ways you can do this -- convert a markdown file into a pdf, convert a folder of markdown files into a folder of pdf files, and convert a folder of markdown files into one combined pdf file.
MD2PDF currently only works with Unix style systems, but I will extend it to Windows shortly.

## Requirements
To run this script on your machine, you will need the following:
* Python 3
* Python Libraries: markdown, pdfkit, argparse, os, re
* Other: wkhtmltopdf

### Installing the required Python libraries
The python libraries can be installed easily thanks to the __requirements.txt__ file. You can install these packages by being in this project directory and running the following command:
```bash
pip install -r requirements.txt
```

### Installing wkhtmltopdf
You'll need to install wkhtmltopdf for this project to run:

For Ubuntu/Linux, install with apt:
```bash
sudo apt-get install wkhtmltopdf
```

For macOS, install with Homebrew:
```bash
brew install wkhtmltopdf
```
You can also download it from wkhtmltopdf.org and follow installation instructions.

## Using MD2PDF
Run the python code using 
```bash
python md2pdf.py
```
The program will prompt you for the following:
1. __Input__: The input for this program are file/folder paths. You can specify a path to a Markdown file (.md), or a folder consisting .md files
2. __Output__: The output for this program are .pdf file paths/folder paths. You can specify a path to a .pdf file, or a folder that will contain the .pdf files
3. __CSS file__: You can specify the path to a .css file for styling your Markdown file



## Styling PDFs with CSS
The resulting PDFs can be styled with CSS. A sample CSS file named __sample.css__ has been included in the project and demonstrates the usage of CSS styling rules to determine the output PDFs. 

## Future Updates 
There are a few future updates planned that can improve upon this tool:
* Syntax coloring in code blocks
* Ignore non .md files inside a folder and process only the .md files

Feel free to suggest new features by opening an issue. 