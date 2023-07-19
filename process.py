import sys
# sys.path.insert(0, 'C:\Users\jrura\Desktop\psc-f')

import subprocess
import json
from translation import parse_code
from download_code import download
from downloads.extract_function import extract_function_contents
from prep_file import prep_file
from postToLeopard import postToLeopard


class ScratchConverter():
    def __init__(self, url) -> None:
        self.scratchURL = url
        self.url = url
        self.codePath = './downloads/downloaded_code.js'
        
    def convert(self):
        with open('ast.json') as f:
            ast = json.load(f)
        parse_code(ast['body'])

    def downloadFunction(self):
        download(self.url)
        extract_function_contents(self.codePath)

    def prepareFunction(self):
        prep_file()

    def callNodeToAST(self):
        if subprocess.run(["node", ".\convertToAST.js"]).returncode == 0:
            print("Success converting to AST")
        else:
            print("Error")
    def leopardConversion(self):
        self.url = postToLeopard(self.url)

    def convertFromScratch(self):
        self.leopardConversion()
        self.downloadFunction()
        self.prepareFunction()
        self.callNodeToAST()
        self.convert()
        print("Done")
        with open('mainCode.scl') as f:
            return f.read()
        

        