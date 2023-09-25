import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import os

def download_file(url):
    urllib.request.urlretrieve(url, os.devnull)
    print(f"下载完成: {url}")

def parse_and_download(json_data):
    data = json.loads(json_data)
    urls = data["4k"]["data"]
    with ThreadPoolExecutor() as executor:
        for item in urls:
            preview_url = item["preview"]
            executor.submit(download_file, preview_url)
    urls = data["live"]["data"]
    with ThreadPoolExecutor() as executor:
        for item in urls:
            preview_url = item["preview"]
            executor.submit(download_file, preview_url)

# 读取JSON文件
with open("result.json") as file:
    json_data = file.read()

# 解析并下载文件
parse_and_download(json_data)
