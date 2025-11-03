# %%
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
from core.services import CachedHttpClient

session = CachedHttpClient()
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def find_sitemap(url):
    response = session.get(url)
    soup = BeautifulSoup(response, "html.parser")

    robots_url = urljoin(url, "/robots.txt")
    robots_content = session.get(robots_url)

    sitemap_start = robots_content.find("Sitemap:")
    if sitemap_start != -1:
        sitemap_end = robots_content.find("\n", sitemap_start)
        sitemap_url = robots_content[sitemap_start + 8 : sitemap_end].strip()
        return sitemap_url

    sitemap_links = soup.find_all(
        "a", href=lambda href: href and "sitemap" in href.lower()
    )
    if sitemap_links:
        return urljoin(url, sitemap_links[0]["href"])


site_url = "https://chromewebstore.google.com/"
sitemap_url = find_sitemap(site_url)
if sitemap_url:
    print(f"Found Sitemap: {sitemap_url}")
else:
    print("Sitemap not found.")
