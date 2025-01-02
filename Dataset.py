import os
import requests
import xml.etree.ElementTree as ET
import zipfile
from tqdm import tqdm

def download_file(url, destination_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(destination_path, 'wb') as file:
        with tqdm(
            total=total_size, 
            unit='B', 
            unit_scale=True, 
            unit_divisor=1024, 
            desc=os.path.basename(destination_path)
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))

def extract_zip(zip_path, destination_folder):
    zip_name = os.path.splitext(os.path.basename(zip_path))[0]
    extract_to = os.path.join(destination_folder, zip_name)
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted: {zip_path} to {extract_to}")

xml_file = "Dataset.meta4"

tree = ET.parse(xml_file)
root = tree.getroot()

namespace = {'ml': 'urn:ietf:params:xml:ns:metalink'}

os.makedirs("downloads", exist_ok=True)
os.makedirs("data", exist_ok=True)

for file in root.findall("ml:file", namespace):
    file_name = file.get("name")
    url = file.find("ml:url", namespace).text

    file_path = os.path.join("downloads", file_name)

    download_file(url, file_path)

    extract_zip(file_path, "data")

print("Download and extraction complete.")
