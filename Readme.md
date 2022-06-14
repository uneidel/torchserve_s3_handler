# Torchserve S3 Custom Handler
Custom Handler for torchserve consuming directly from S3 

This is a quick and dirty torchserve custom Handler consuming and returning processed data directly from s3. this is useful when handling with large files.



## Prerequisites 

1) Create venv
2) pip3 install torchserve torch 

## Install minio 

1) Run Container
Run Container: podman run \
  -p 9000:9000 \
  -p 9001:9001 \
  minio/minio server /data --console-address ":9001"

2) Create Tenant 
3) Store Url AccessKey and SecretKey as environtvariables

    S3Url=localhost
    S3AccessKey=GBDWDOWNDWDNIDWNI
    S3SecretKey=dkjwqnkldnqwdnqwdnqw


## Upload Sample Picture
1) cd ./tools/
2) python3 s3tool.py upload ../assets/dog.jpg
3) Note done resulting bucketName 
BucketName created: 80e92e51-2ee7-40b4-9f20-e1b9a8a30a55
File: ../assets/dog.jpg uploaded

## Run Torchserve

make run

Please note default uses CPU if you want to use gpu remove --ts-config config.properties in makefile

## Use Curl 
Please replace bucketname 

curl -H "Content-Type: application/json" -X POST "http://localhost:8080/predictions/hdr" -d '{"bucket":"80e92e51-2ee7-40b4-9f20-e1b9a8a30a55", "file":"dog.jpg"}'

results in 
{
  "executionTime": 5.503670930862427,
  "bucket": "80e92e51-2ee7-40b4-9f20-e1b9a8a30a55",
  "filename": "dog.jpg",
  "Success": true
}

Change curl to e.g. 

curl -H "Content-Type: application/json" -X POST "http://localhost:8080/predictions/hdr" -d '{"bucket":"80e92e51-2ee7-40b4-9f20-e1b9a8a30a55", "file":"dog.jpg", "config": { "tone_map: "mantiuk"}}'

to change Configuration please see full opts in handler.py


## Download Results 
1) cd ./tools
2) python3 s3tool.py read  "80e92e51-2ee7-40b4-9f20-e1b9a8a30a55"


All Credits for Expandnet goes to https://github.com/dmarnerides

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.