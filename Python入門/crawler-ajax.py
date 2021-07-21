# 抓取 medium.com 的文章資料
import urllib.request as req
url="http://www.facebook.com.tw/"
# 建立一個 request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read() # 根據觀察，取得的資料是 JSON 格式
# 解析 JSON 格式的資料，取得每篇文章的標題
import json
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式
# 取得 JSON 資料中的文章標題