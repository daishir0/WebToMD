# WebToMD

## Overview
WebToMD is a Python script that converts web pages to Markdown format. It fetches the content of a given URL, converts the HTML to Markdown, and saves it as a text file.

## Installation
To install WebToMD, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/daishir0/WebToMD
   ```
2. Change to the project directory:
   ```
   cd WebToMD
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use WebToMD, run the script from the command line with a URL as an argument:

```
python webtomd.py <URL>
```

For example:
```
python webtomd.py https://example.com
```

The script will create a Markdown file in the same directory, with the filename derived from the URL.

## Notes
- Ensure you have permission to scrape the website you're targeting.
- Some websites may block web scraping attempts.
- The quality of the Markdown output may vary depending on the structure of the original HTML.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# WebToMD

## 概要
WebToMDは、ウェブページをMarkdown形式に変換するPythonスクリプトです。指定されたURLのコンテンツを取得し、HTMLをMarkdownに変換して、テキストファイルとして保存します。

## インストール方法
WebToMDをインストールするには、以下の手順に従ってください：

1. リポジトリをクローンします：
   ```
   git clone https://github.com/daishir0/WebToMD
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd WebToMD
   ```
3. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

## 使い方
WebToMDを使用するには、コマンドラインからURLを引数としてスクリプトを実行します：

```
python webtomd.py <URL>
```

例：
```
python webtomd.py https://example.com
```

スクリプトは、URLから派生したファイル名で、同じディレクトリにMarkdownファイルを作成します。

## 注意点
- スクレイピング対象のウェブサイトの許可を得ていることを確認してください。
- 一部のウェブサイトはウェブスクレイピングの試みをブロックする場合があります。
- Markdown出力の品質は、元のHTMLの構造によって異なる場合があります。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
