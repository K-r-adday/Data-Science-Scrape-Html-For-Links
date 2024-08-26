from bs4 import BeautifulSoup
import sys

def extract_links(input_file, output_file):
    # Read the HTML content from the file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Extract all href attributes from <a> tags
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Write the extracted links to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python h2u.py <input_file.html> <output_file.txt>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        extract_links(input_file, output_file)
