import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup
from datetime import timedelta, date
from unidecode import unidecode

year = int(input("Enter year:"))

datelist = []

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(year, 1, 1)
end_dt = date(year, 12, 31)
for dt in daterange(start_dt, end_dt):
    datelist.append(dt.strftime("%Y/%m/%d"))

def addjw(text):
	return """https://wol.jw.org/en/wol/h/r1/lp-e/""" + text

linklist = list(map(addjw, datelist))

def writetofile(html):
	soup = BeautifulSoup(html, "lxml")
	text = soup.find("h2")
	text = unidecode(text.get_text())
	text = text.replace(",", "").replace('MEMORIAL DATEAfter Sundown', '')
	text2 = soup.find("p", class_ = "themeScrp")
	text2 = unidecode(text2.get_text())
	text2 = text2.replace("--", "-")
	with open("///storage/emulated/0/Kustom/Daily text/{0} {1}.txt".format(text, year), "w") as f:
		f.write(text2)
	return text

async def download_site(session, url):
    async with session.get(url) as response:
        body = await response.text()
        print(writetofile(body))

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = linklist
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")