# MD2PDF

MD2PDF is a CLI Tool created with Python 3 that allows you to convert your markdown documents into pdfs. There are several ways you can do this -- convert a markdown file into a pdf, convert a folder of markdown files into a folder of pdf files, and convert a folder of markdown files into one combined pdf file.
MD2PDF currently only works with Unix style systems, but I will extend it to Windows shortly.

##### Table of Contents  
* [Requirements](#requirements)  
* [Usage](#usage)  
* [Styling your PDF](#styling)  
* [Future Updates and Contribution](#future)  


<a name="requirements"/>

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

<a name="usage"/>

## Using MD2PDF
Run the python code using 
```bash
python md2pdf.py
```
The program will prompt you for the following:
1. __Input__: The input for this program are file/folder paths. You can specify a path to a Markdown file (.md), or a folder consisting .md files
2. __Output__: The output for this program are .pdf file paths/folder paths. You can specify a path to a .pdf file, or a folder that will contain the .pdf files. The folder does not need to already exist as the program can create a new folder for you.
3. __CSS file__: You can specify the path to a .css file for styling your Markdown file

There are different outcomes of specifying files and folders as input and output:
1. If you specify an .md __file as input__ and specify a .pdf __file as output__, then the __.md file is converted into a .pdf file__.
2. If you specify a __folder as input__ and specify a __folder as output__ , then the __.md files in the input folder are converted to .pdf files in the output folder__
3. If you specify a __folder as input__ and specify a .pdf __file as output__, then the __.md files in the input folder are combined into a single .pdf file__.

MD2PDF also supports inline HTML, so utilizing different div tags with different classes could allow even more customization through CSS.

<a name="styling"/>

## Styling PDFs with CSS
The resulting PDFs can be styled with CSS. Fonts, colors, sizes, stroke, etc. of each element in your generated PDF can all be customized as per your liking. A sample CSS file named __sample.css__ has been included in the project and demonstrates the usage of CSS styling rules to determine the styling of the output PDFs. 

<a name="future"/>

## Future Updates 
There are a few future updates planned that can improve upon this tool:
* Syntax coloring in code blocks
* Ignore non .md files inside a folder and process only the .md files
* MD2PDF will be available through HomeBrew soon

Feel free to suggest new features or bugs by opening an issue. This project is open to contributions! :) Contributions are also open to help with the future updates.