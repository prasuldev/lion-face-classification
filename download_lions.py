from bing_image_downloader import downloader

downloader.download(
    "lion face",          # search term
    limit=100,            # number of images
    output_dir="data",    # folder to save images
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)


f