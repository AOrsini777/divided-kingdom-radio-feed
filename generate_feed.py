import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://gsradio.net/shows/divided_kingdom/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
audio_links = soup.find_all('a', href=True)
audio_urls = [link['href'] for link in audio_links if link['href'].endswith('.mp3')]

rss_content = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
    <title>Divided Kingdom Podcast</title>
    <link>https://gsradio.net/shows/divided_kingdom/</link>
    <description>Episodes of the Divided Kingdom show</description>
    <language>en-us</language>"""

for url in audio_urls:
    rss_content += f"""
    <item>
        <title>Episode</title>
        <link>{url}</link>
        <enclosure url="{url}" type="audio/mpeg" />
        <guid>{url}</guid>
        <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
    </item>"""

rss_content += """
</channel>
</rss>"""

with open("feed.xml", "w") as f:
    f.write(rss_content)