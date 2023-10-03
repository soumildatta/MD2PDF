from typing_extensions import Required
import markdown 
import pdfkit 
import argparse
import os 

def list_files(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def convert(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    pdfkit.from_string(html_content, output_file)

def process_folder_into_folder(input_folder, output_folder):
    # make the folder to output the pdfs into
    file_list = list_files(input_folder)
    os.makedirs(output_folder, exist_ok=True)

    for file in file_list:
        output_file = file.split('.')[0]
        convert(f'{input_folder}/{file}', f'{output_folder}/{output_file}.pdf')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF.')
    parser.add_argument('--type', type=int, required=False, help='1 to process a file, 2 to process a folder')
    parser.add_argument('--input', type=str, required=True, help='Input Markdown file or folder.')
    parser.add_argument('--output', type=str, required=True, help='Output PDF file.')

    args = parser.parse_args()

    type = args.type
    input_file = args.input
    output_file = args.output

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)

    # Perform conversion
    if type == 1:
        convert(input_file, output_file)
    else:
        process_folder_into_folder(input_file, output_file)
    print(f"Successfully converted '{input_file}' to '{output_file}'.")