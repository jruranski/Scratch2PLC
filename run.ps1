# Load the project
# node .\convert_project.js
python .\download_code.py https://codesandbox.io/s/jweobj/
python .\downloads\extract_function.py
# prepare file for translation to ast
python .\prep_file.py
# translate to ast
node .\convertToAST.js
# translate to SCL
jupyter nbconvert --to script .\translation.ipynb
python .\translation.py
# Create the Openness source files

