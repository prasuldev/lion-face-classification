from bing_image_downloader import downloader
import os

# Make sure folders exist
os.makedirs("data/train/not_lions", exist_ok=True)
os.makedirs("data/val/not_lions", exist_ok=True)

# Download training images
downloader.download("cat", limit=20, output_dir="data/train/not_lions", adult_filter_off=True, force_replace=False, timeout=60)

# Download validation images
downloader.download("cat", limit=5, output_dir="data/val/not_lions", adult_filter_off=True, force_replace=False, timeout=60)

print("Non-lion images downloaded successfully!")