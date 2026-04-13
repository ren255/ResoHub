import os
from storages.backends.s3boto3 import S3Boto3Storage


def _build_url(name, location):
    """
    開発: http://localhost:3902          → http://resohub-bucket.web.garage.localhost:3902/static/...
    本番: https://cdn.yourdomain.com     → https://resohub-bucket.cdn.yourdomain.com/static/...
    """
    public_url = os.getenv("AWS_S3_PUBLIC_URL", "")
    bucket = os.getenv("AWS_STORAGE_BUCKET_NAME", "")

    # http://localhost:3902 → scheme=http, host=localhost:3902
    scheme, host = public_url.split("://")
    return f"{scheme}://{bucket}.web.{host}/{location}/{name}"


class StaticS3Boto3Storage(S3Boto3Storage):
    location = "static"
    querystring_auth = False

    def url(self, name, parameters=None, expire=None, http_method=None):
        return _build_url(name, self.location)


class S3MediaStorage(S3Boto3Storage):
    location = "media"
    querystring_auth = False

    def url(self, name, parameters=None, expire=None, http_method=None):
        return _build_url(name, self.location)
