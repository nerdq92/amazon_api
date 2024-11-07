import streamlit as st
from bs4 import BeautifulSoup
import requests
import json

def fetch_open_graph_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    #     "Accept-Language": "en-US,en;q=0.9",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #     "Connection": "keep-alive",
    # }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract Open Graph properties
    tag = soup.find('img', {'id': 'landingImage'})
    if tag and tag.has_attr('data-a-dynamic-image'):
        data_dynamic_image = json.loads(tag['data-a-dynamic-image'])
        title = tag['alt']
        image_url = list(data_dynamic_image.keys())[0]
    return soup
try:
    soup = fetch_open_graph_data('https://www.amazon.in/Complete-Novels-Sherlock-Holmes/dp/8175994312/ref=zg_bs_g_1318054031_d_sccl_1/000-0000000-0000000?psc=1')
    st.write(soup)
except:
    st.write('Error occur')
