from bs4 import BeautifulSoup
import requests

myHtml = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <h1>This is h1</h1>
    <h1>This is another h1 tag</h1>
    <h2>This is h2 (a bit smaller than h1)</h2>
    <p>I'm Henry.</p>
</body>
</html>'''

req = requests.get('http://www.baidu.com').content
soup = BeautifulSoup(req, 'html.parser')
links = soup.findAll('a')
for i in links:
    print(i.string)
