
import urllib.request
import re
import sys


def extract_id_from_url(url):
    # Extract the ID from the URL using regular expressions
    pattern = r'https://codesandbox\.io/s/([^/?]+)'
    match = re.search(pattern, url)

    if match:
        id = match.group(1)
        return id

    return None

def generate_link_with_id(id):
    base_link = 'https://{}.csb.app/Sprite1/Sprite1.js'.format(id)
    return base_link


#mainUrl = 'https://codesandbox.io/s/me5p8y/'

def download(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

  
    if len(sys.argv) > 1:
        mainUrl = sys.argv[1]
    else:
        mainUrl = 'https://codesandbox.io/s/me5p8y/'
    if url is not None:
        mainUrl = url   
    print("URL:", mainUrl)
    id = extract_id_from_url(mainUrl)
    url = ''
    if id:
        url = generate_link_with_id(id)
        print("Generated URL:", url)
    else:
        print("Error extracting ID from URL.")
        


    destination_file = './downloads/downloaded_code.js'

    try:
        urllib.request.urlretrieve(url, destination_file)
        print("Code downloaded successfully!")
    except Exception as e:
        print("Error downloading code:", str(e))

if __name__ == "__main__":
    download(None)
    

# download_code(url, destination_file)