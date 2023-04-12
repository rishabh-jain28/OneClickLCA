import requests
import os
from tqdm import tqdm
from lxml import html
from furl import furl
import tabula
import pandas as pd
url = 'https://www.greenbooklive.com/search/companysearch.jsp?from=0&partid=10028&sectionid=%200&companyName=&productName=&productType=&certNo=&regionId=0&countryId=0&addre%20ssPostcode=&certBody=&id=260&results_pp=1000&sortResultsComp='


pdf_xpath = '//a[contains(@href, ".pdf")]/@href'

save_dir = 'pdf_files'

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

response = requests.get(url)
tree = html.fromstring(response.content)
_links = tree.xpath(pdf_xpath)
f = furl(url)
domain = f.host
pdf_links = ['https://'+domain + '/' + i.split('/..')[0] for i in _links]


save_dir = 'pdf_files'

for pdfs in pdf_links:


    if not os.path.exists(save_dir):
        os.makedirs(save_dir)


    filename = os.path.join(save_dir, os.path.basename(pdfs))


    response = requests.get(pdfs, stream=True)


    file_size = int(response.headers.get('content-length', 0))


    chunk_size = 1024
    num_bars = int(file_size / chunk_size)
    with open(filename, 'wb') as f, tqdm(total=file_size, unit='B', unit_scale=True, desc=filename) as pbar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            pbar.update(len(chunk))



