import re

def process_js_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # matches any word characters followed by ++ and replace with the equivalent assignment operation
    updated_content = re.sub(r'(\w+)\+\+', r'\1 = \1 + 1', content)

 # erases any occurrence of 'this.stage.vars'
    updated_content = re.sub(r'this\.stage\.vars\.', '', updated_content)

    with open(file_path, 'w') as file:
        file.write(updated_content)

# Use the function
def prep_file():
    process_js_file('leopard.js')

if __name__ == "__main__":
    prep_file()