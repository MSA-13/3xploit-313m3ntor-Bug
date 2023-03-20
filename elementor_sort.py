import requests
import re

url = input("Enter URL: ")

response = requests.get(url)

if response.status_code == 200:
    pattern = re.compile(r"src='(.*?)'")
    matches = pattern.findall(response.text)
    elementor_urls = [url for url in matches if 'elementor' in url]
    sorted_urls = sorted(elementor_urls)
    with open("sorted_urls.txt", "w") as f:
        f.write("\n".join(sorted_urls))
else:
    print(f"Error: {response.status_code}")
    
