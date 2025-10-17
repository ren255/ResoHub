import hashlib
import json
import requests
from django.core.cache import cache


class CachedHttpClient:
    def __init__(self, expire_after=60 * 60 * 24 * 30):
        # month
        self.expire_after = expire_after

    def get(self, url, **kwargs):
        cache_key = self._cache_key(url, **kwargs)

        cached = cache.get(cache_key)
        if cached is not None:
            return cached

        result = self._fetch(url, **kwargs)
        cache.set(cache_key, result, self.expire_after)
        return result

    def _cache_key(self, url, **kwargs):
        key_data = f"{url}:{json.dumps(kwargs, sort_keys=True)}"
        hash_key = hashlib.md5(key_data.encode()).hexdigest()
        return f"http_cache:{hash_key}"

    def _fetch(self, url, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.text
