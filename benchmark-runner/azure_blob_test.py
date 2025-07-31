from azure.storage.blob import BlobServiceClient
import time
import os

CONNECT_STR = "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"  # CHANGE this
CONTAINER_NAME = "benchmark-container"  # Must already exist
TEST_FILE = "testfile.txt"
UPLOAD_SIZE_MB = 10

def generate_test_file():
    with open(TEST_FILE, "wb") as f:
        f.write(os.urandom(UPLOAD_SIZE_MB * 1024 * 1024))

def upload_blob():
    blob_service = BlobServiceClient.from_connection_string(CONNECT_STR)
    container_client = blob_service.get_container_client(CONTAINER_NAME)

    start = time.time()
    with open(TEST_FILE, "rb") as data:
        container_client.upload_blob(TEST_FILE, data, overwrite=True)
    end = time.time()

    return round(end - start, 2)

def download_blob():
    blob_service = BlobServiceClient.from_connection_string(CONNECT_STR)
    container_client = blob_service.get_container_client(CONTAINER_NAME)

    start = time.time()
    blob_data = container_client.download_blob(TEST_FILE)
    with open("downloaded_" + TEST_FILE, "wb") as f:
        f.write(blob_data.readall())
    end = time.time()

    return round(end - start, 2)

if __name__ == "__main__":
    generate_test_file()

    upload_time = upload_blob()
    download_time = download_blob()

    print(f"✅ Azure Upload Time: {upload_time} seconds")
    print(f"✅ Azure Download Time: {download_time} seconds")

    os.makedirs("../results", exist_ok=True)
    with open("../results/azure_results.txt", "w") as f:
        f.write(f"Upload Time: {upload_time} sec\n")
        f.write(f"Download Time: {download_time} sec\n")