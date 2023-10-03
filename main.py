import markdown 
import pdfkit 
import argparse
import os 

def convert(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    pdfkit.from_string(html_content, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF.')
    parser.add_argument('--input', type=str, required=True, help='Input Markdown file.')
    parser.add_argument('--output', type=str, required=True, help='Output PDF file.')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)

    # Perform conversion
    convert(input_file, output_file)
    print(f"Successfully converted '{input_file}' to '{output_file}'.")