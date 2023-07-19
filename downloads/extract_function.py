# import re

def extract_function_contents(js_file_path):
    with open(js_file_path, 'r') as file:
        js_code = file.read()

    start_keyword = '*whenGreenFlagClicked() {'
    end_keyword = '}'
    start_index = js_code.find(start_keyword)
    if start_index == -1:
        print("Function not found in the JavaScript code.")
        return
    start_index += len(start_keyword)

    # Initialize brace count to 1 for the initial opening brace
    brace_count = 1
    i = start_index
    while brace_count > 0 and i < len(js_code):
        if js_code[i] == '{':
            brace_count += 1
        elif js_code[i] == '}':
            brace_count -= 1
        i += 1

    if brace_count != 0:
        print("Unbalanced braces in the JavaScript code.")
        return

    function_contents = js_code[start_index:i-1].strip()  # subtract 1 from i to exclude the final closing brace

    # Save the extracted contents to a separate file
    with open('leopard.js', 'w') as output_file:
        output_file.write(function_contents)
    print("Function contents extracted and saved to 'leopard.js' file.")


# Usage
js_file_path = './downloads/downloaded_code.js'  # Replace with the path to your JavaScript file
extract_function_contents(js_file_path)
