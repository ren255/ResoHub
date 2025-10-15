from django.test import TestCase

# Create your tests here.
import time
from services import CachedHttpClient

session = CachedHttpClient()

for i in range(10):
    start = time.time()
    html = session.get("https://www.google.com")
    end = time.time()
    print(f"Request {i+1}: {end - start:.4f} seconds")