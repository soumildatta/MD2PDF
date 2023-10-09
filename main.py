import markdown 
import pdfkit 
import argparse
import os 
import re

def preprocess_markdown(markdown_content):
    # Use regex to remove the language identifiers from code fences
    return re.sub(r"```(\w+)\n", "```\n", markdown_content)

def list_files(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def convert(input_file, output_file, css_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
        
    markdown_content = preprocess_markdown(markdown_content)
    pdfkit.from_string(markdown.markdown(markdown_content), output_file, css=css_file)

def convert_combined(input_folder, output_file, css_file):
    file_list = list_files(input_folder)

    html_content = ""
    for file in file_list:
        file = f'{input_folder}/{file}'
        with open(file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        markdown_content = preprocess_markdown(markdown_content)
        html_content += markdown.markdown(markdown_content)

    pdfkit.from_string(html_content, output_file, css=css_file)

def process_folder_into_folder(input_folder, output_folder, css_file):
    # make the folder to output the pdfs into
    file_list = list_files(input_folder)
    os.makedirs(output_folder, exist_ok=True)

    for file in file_list:
        output_file = file.split('.')[0]
        convert(f'{input_folder}/{file}', f'{output_folder}/{output_file}.pdf', css_file)

def process_folder_into_file(input_folder, output_file, css_file):
    convert_combined(input_folder, output_file, css_file)

if __name__ == "__main__":
    input_item = input('Input markdown file or folder: ')
    output_item = input('Input name of output pdf, or a folder to output pdfs to: ')
    css_item = input('CSS File: ')

    # Check if input file exists
    if not os.path.exists(input_item):
        print(f"Error: Input file '{input_item}' not found.")
        exit(1)

    # Perform conversion
    split_input = input_item.split('.')
    split_output= output_item.split('.')

    type = ''
    if len(split_input) > 1:
        if split_input[-1] == 'md':
            if split_output[-1] == 'pdf':
                type = 'single'
        else:
            if split_output[-1] == 'pdf':
                type = 'combined'
            else:
                type = 'folder'

    if type == 'single':
        convert(input_item, output_item, css_item)
    elif type == 'combined':
        process_folder_into_file(input_item, output_item, css_item)
    else:
        process_folder_into_folder(input_item, output_item, css_item)

    print(f"Successfully converted '{input_item}' to '{output_item}'.")