import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def url_to_markdown(url):
    response = requests.get(url)
    response.raise_for_status()  # URLが正しいか確認

    soup = BeautifulSoup(response.content, 'html.parser')
    markdown_text = md(str(soup))

    # URLをファイル名に変換
    file_name = url.replace('http://', '').replace('https://', '').replace('/', '_') + '.txt'
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_text)
    
    print(f"Markdownファイルが {file_name} として保存されました。")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("使用法: python getmd.py ")
    else:
        url_to_markdown(sys.argv[1])
      
