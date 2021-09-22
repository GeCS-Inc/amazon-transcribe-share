import json
import os
import time

import boto3
import requests
from botocore.exceptions import ClientError


BUCKET_NAME = "your-bucket-name"
REGION_NAME = "us-east-2"
AUDIO_FILE = "sample.wav"

def amazon_transcribe(file_name, bucket, region, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return None

    job_uri = f"s3://{bucket}/{object_name}"
    job_name = "sample_job"
    print("job_uri", job_uri)

    transcribe = boto3.client('transcribe', region_name=region)
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode='ja-JP'
    )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        trans_job_status = status['TranscriptionJob']['TranscriptionJobStatus']
        if trans_job_status in ['COMPLETED', 'FAILED']:
            print(f"job status: {trans_job_status}")
            break
        print("Not ready yet...")
        time.sleep(5)

    if trans_job_status == "FAILED":
        return None

    output_json_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    output_json = requests.get(output_json_url).json()
    return output_json

if __name__ == "__main__":
    result = amazon_transcribe(AUDIO_FILE, bucket=BUCKET_NAME, region=REGION_NAME)
    with open("output.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
