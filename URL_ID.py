import pandas as pd
from bs4 import BeautifulSoup
import os

# Read the input Excel file
df = pd.read_excel('input.xlsx')

for index, row in df.iterrows():
    url_id = row['URL_ID']
    html_content = row['HTML_Content']

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the article title and text
    article_title = soup.find('title').text
    article_text = ' '.join([p.text for p in soup.find_all('p')])

    # Create a directory to store the text files if it doesn't exist
    if not os.path.exists('article_texts'):
        os.makedirs('article_texts')

    # Save the extracted text to a text file
    with open(f'article_texts/{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(f'{article_title}\n\n{article_text}')
