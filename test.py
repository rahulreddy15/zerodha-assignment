import os
from datetime import datetime
import requests
from zipfile import ZipFile
from io import BytesIO

# import os
# os.path.abspath(os.getcwd())

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y")
splitDate = dt_string.split("/")
D, M, Y = splitDate[0], splitDate[1], splitDate[2][2:]
print(D+M+Y)
print(dt_string)
# https://www.bseindia.com/download/BhavCopy/Equity/EQ100521_CSV.ZIP

headers_dict = {"Host": "www.bseindia.com",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx",
                "Upgrade-Insecure-Requests": "1",
                "TE": "Trailers"
                }
EQUITY_DATE = "060521"
URL = "https://www.bseindia.com/download/BhavCopy/Equity/EQ" + EQUITY_DATE + "_CSV.ZIP"
url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ100521_CSV.ZIP"

r = requests.get(url, headers=headers_dict)
# print(r.content)
z = ZipFile(BytesIO(r.content))
z.extractall(path="CSV_FILES")
