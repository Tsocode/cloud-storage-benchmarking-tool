import boto3
import time
import os

BUCKET_NAME = "cloud-benchmark-bucket-yourname"  # CHANGE this
TEST_FILE = "testfile.txt"
UPLOAD_SIZE_MB = 10

# Replace with your AWS access keys or use environment variables
AWS_ACCESS_KEY = "YOUR_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"

def generate_test_file():
    with open(TEST_FILE, "wb") as f:
        f.write(os.urandom(UPLOAD_SIZE_MB * 1024 * 1024))

def upload_blob():
    s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    start = time.time()
    s3.upload_file(TEST_FILE, BUCKET_NAME, TEST_FILE)
    end = time.time()

    return round(end - start, 2)

def download_blob():
    s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    start = time.time()
    s3.download_file(BUCKET_NAME, TEST_FILE, "downloaded_" + TEST_FILE)
    end = time.time()

    return round(end - start, 2)

if __name__ == "__main__":
    generate_test_file()

    upload_time = upload_blob()
    download_time = download_blob()

    print(f"✅ S3 Upload Time: {upload_time} seconds")
    print(f"✅ S3 Download Time: {download_time} seconds")

    os.makedirs("../results", exist_ok=True)
    with open("../results/s3_results.txt", "w") as f:
        f.write(f"Upload Time: {upload_time} sec\n")
        f.write(f"Download Time: {download_time} sec\n")