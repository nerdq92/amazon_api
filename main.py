import streamlit as st
from bs4 import BeautifulSoup
import requests
import json
import random

def fetch_books_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }
    response = requests.get(url,headers=headers)
    data = BeautifulSoup(response.content, 'html.parser')
    img_tags = data.find_all("img", class_="lazyload img-responsive center-block")
    # data_image = img_tag.get("data-src")
    # alt_text = img_tag.get("alt")
    return img_tags

st.title("Book Search")
url = st.text_input("Enter a site url")

if st.button("Search"):
    img_tags = fetch_books_data(url)
    st.write(img_tags)
    random_element = random.choice(img_tags)
    st.write(random_element.get("data-src")
    st.write(random_element.get("alt")
    
    # st.write(data)
    # st.write(alt_text)
    # st.image('https:'+data_image,width=250)    
