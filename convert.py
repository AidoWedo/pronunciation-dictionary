# Example Python code to convert a text based file with word followed by Internation Phonetic Alphabet

def generate_pls_xml_from_file(file_path):
    # Reading the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # XML header and root element
    pls_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0" 
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon 
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
      alphabet="ipa" xml:lang="en-GB">
"""

# Process each line to extract grapheme (word) and phoneme (pronunciation)
    for line in lines:
        parts = line.strip().split(' - ')
        if len(parts) == 2:
            grapheme = parts[0].strip()
            phoneme = parts[1].strip()
            pls_xml += f"""
  <lexeme>
    <grapheme>{grapheme}</grapheme>
    <phoneme>{phoneme}</phoneme>
  </lexeme>
"""

# Closing the root element
    pls_xml += "</lexicon>"

    return pls_xml.strip()

# Example usage
file_path = 'path_to_your_file.txt'  # Specify the path to your text file
pls_xml_content = generate_pls_xml_from_file(file_path)

# Optionally, write the generated XML content to a new XML file
output_file_path = 'output_pronunciation_lexicon.xml'
with open(output_file_path, "w") as output_file:
    output_file.write(pls_xml_content)

print("PLS XML content has been generated and saved.")
