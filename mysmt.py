import xmlrpc.client
import sys

def translate_file(input_file, output_file):
    # Connect to the Moses server
    server = xmlrpc.client.ServerProxy("http://localhost:8080/RPC2")
    
    try:
        # Read input text from file
        with open(input_file, 'r', encoding='utf-8') as infile:
            input_text = infile.read().strip()
        
        # Send a translation request
        response = server.translate({"text": input_text})
        translated_text = response['text']
        
        # Write translated text to output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_text)
        
        print("Translation successful. Output saved to:", output_file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        translate_file(input_file, output_file)

