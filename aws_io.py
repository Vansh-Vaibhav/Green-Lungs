"""aws_io.py - AWS integration for Green Lungs.

Amazon S3:               DATA_BUCKET (+ DATA_PREFIX, default "data/") -> CSV datasets downloaded at startup.
Amazon Location Service: GEOCODER=amazon (+ AWS_REGION) -> place names resolved by AWS, Nominatim as fallback.
Both are optional: with no environment variables the app runs fully locally.
"""
import os
import tempfile
from pathlib import Path

DATA_FILES = ["locations.csv", "environment_conditions.csv", "tree_species.csv", "planting_patches.csv",
              "geocode_cache.csv"]


def resolve_data_dir(local_dir: Path):
    """Return (directory holding the CSVs, human-readable source)."""
    bucket = os.getenv("DATA_BUCKET")
    if not bucket:
        return local_dir, "local folder"
    import boto3
    from botocore.exceptions import ClientError
    prefix = os.getenv("DATA_PREFIX", "data/").lstrip("/")
    if prefix and not prefix.endswith("/"):
        prefix += "/"
    dest = Path(tempfile.gettempdir()) / "greenlungs-data"
    dest.mkdir(exist_ok=True)
    s3 = boto3.client("s3", region_name=os.getenv("AWS_REGION") or None)
    for name in DATA_FILES:
        try:
            s3.download_file(bucket, prefix + name, str(dest / name))
        except ClientError:
            if name != "geocode_cache.csv":      # the cache is optional
                raise
    return dest, f"Amazon S3 (s3://{bucket}/{prefix})"


class _AmazonLocation:
    def __init__(self):
        import boto3
        self.client = boto3.client("geo-places", region_name=os.getenv("AWS_REGION") or None)
        self.bias = [float(os.getenv("BIAS_LON", 77.2)), float(os.getenv("BIAS_LAT", 28.6))]  # Delhi

    def geocode(self, query: str):
        r = self.client.search_text(QueryText=query, BiasPosition=self.bias, MaxResults=1)
        items = r.get("ResultItems") or []
        if not items:
            raise ValueError(f"No result for '{query}'")
        lon, lat = items[0]["Position"]
        return lat, lon, items[0].get("Title", query)


class _Fallback:
    def __init__(self, primary, secondary):
        self.primary, self.secondary = primary, secondary

    def geocode(self, query: str):
        try:
            return self.primary.geocode(query)
        except Exception:
            return self.secondary.geocode(query)


def build_geocoder(cache_path: Path):
    """Return (geocoder, name)."""
    from tree_recommender import Geocoder
    osm = Geocoder(cache_path)
    if os.getenv("GEOCODER", "").lower() == "amazon":
        return _Fallback(_AmazonLocation(), osm), "Amazon Location Service"
    return osm, "OpenStreetMap Nominatim"
