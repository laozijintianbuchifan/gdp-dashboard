import streamlit as st
import pandas as pd
import math
from pathlib import Path
import requests
from lxml import etree

url = "https://q.10jqka.com.cn/gn/detail/field/199112/order/desc/page/2/ajax/1/code/308016"

payload = {}
headers = {
  'Accept': 'text/html, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': 'spversion=20130314; _ga=GA1.1.1589657450.1724071969; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=Xv%2BiACHfMqImFGDWTrtiIIPO6khZXkls35aAYsbVGru5I0qmXNIH8pNG0YmFsXOKHi80LrSsTFH9a%2B6rtRvqGg%3D%3D; u_did=4D4028E4EDAF492D9B8BF386EDC20E4D; u_ttype=WEB; user=MDptb183MjkyNTM5Njg6Ok5vbmU6NTAwOjczOTI1Mzk2ODo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA6Ojo6NzI5MjUzOTY4OjE3MjQwNzIzODU6OjoxNzI0MDcyMjgwOjYwNDgwMDowOjFjYTFkNWE5NTBmZTdmNmQ0NmRiM2E0OTIwMGI2Y2QyZDpkZWZhdWx0XzQ6MQ%3D%3D; userid=729253968; u_name=mo_729253968; escapename=mo_729253968; ticket=28f2815bd7ef1716e2f0f1967ca80a9d; user_status=0; utk=f11e171b152ba6181887d1adb1c9ea2b; quantoken=acb3c26a52dda616b66b5843608cb0700a642bb5b327a8b82874f4a6fad88d039be2b057b2d9cbfd771144a3d33db5f8264cc03e20dc5c88b4cead8613cee28ce45a0a5325c2a229eb24bf5dbbaaa890; searchGuide=sg; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1724069167,1724080363; historystock=001298%7C*%7C300468%7C*%7C002369%7C*%7C600839; _ga_KQBDS1VPQF=GS1.1.1724080743.3.1.1724082501.0.0.0; v=Ay2F4K6aN0jAXtOkQXByWB1dPMKiimVP67_FNG8za2c320M8N9pxLHsO1QP8',
  'Referer': 'https://q.10jqka.com.cn/gn/detail/code/308016/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'hexin-v': 'Ay2F4K6aN0jAXtOkQXByWB1dPMKiimVP67_FNG8za2c320M8N9pxLHsO1QP8',
  'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

st.write(response.text)
st.write("aaaaaa")
