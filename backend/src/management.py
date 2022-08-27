import typer
import httpx
from pathlib import Path

app = typer.Typer()

BASE_DOWNLOAD_URL = "http://snap.stanford.edu/data/amazon/productGraph"
METADATA_URL= f"{BASE_DOWNLOAD_URL}/categoryFiles/meta_Electronics.json.gz"
IMAGES_URL = f"{BASE_DOWNLOAD_URL}/image_features/categoryFiles/image_features_Electronics.b"

DOWNLOAD_FOLDER = "/usr/src/app/productsdata"

def file_exists(file_path:Path)->bool:
    """Check is the file already exists in the folder"""
    return file_path.exists()

def download_files(url:str) -> None:
    """Download large files """
    download_path = Path(DOWNLOAD_FOLDER).joinpath(url.split('/')[-1])

    if not file_exists(download_path):
        with open(download_path, 'wb') as download_file:
            print("Downloading file ....")
            with httpx.stream('GET', url) as response:
                for chunk in response.iter_bytes():
                    download_file.write(chunk)
            print("File downloaded")

@app.command()
def download_metadata_files()->None:
    download_files(METADATA_URL)

@app.command()
def download_images_files()->None:
    download_files(METADATA_URL)

def seed_elasticsearc():
    pass



if __name__ == "__main__":
    app()
