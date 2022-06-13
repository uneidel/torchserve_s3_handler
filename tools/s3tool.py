from minio import Minio
from minio.error import S3Error
import uuid
import sys
import os
def CreateAndUpload(client, filepath):
    bucket =  str(uuid.uuid4())
    
    found = client.bucket_exists(bucket)
    if not found:
        client.make_bucket(bucket)
  
    client.fput_object(bucket, "dog.jpg", filepath,)
    print("BucketName created: %s" % (bucket))
    print("File: %s uploaded" % filepath )
    
def Read(client, bucketname):
    
    bucket = bucketname 
    print("BucketName: %s" % (bucket))
    
    
    objects = client.list_objects(bucket)   
    for obj in objects:
        print("%s;%i Byte" % (obj.object_name, obj.size))
        client.fget_object(bucket,obj.object_name,obj.object_name)
    
    
    client.fget_object(bucket,"processed.jpg", "./processed.jpg")
   
class MinioHandler():
    
    def __init__(self) -> None:
        pass
    
    def Connect(self,url, accesskey, accesssecret):
        self.client = Minio(
        url,
        access_key=accesskey, # hier natürliuch os.env
        secret_key=accesssecret, # hier auch
        secure=True
        )
        
    def CreateBucket(self,BucketName,Createifnotexists=True):       
        found = self.client.bucket_exists(BucketName)
        if not found and Createifnotexists is True:
            self.client.make_bucket(BucketName)
            
    def Upload(self, BucketName, UploadName, LocalFile):
        self.client.fput_object(BucketName, UploadName, LocalFile)
        
    

if __name__ == "__main__":
    try:
        s3url = os.environ.get("S3Url", "storage.XXXXXX.com")
        s3accesskey = os.environ.get("S3AccessKey", "B6XXXXXXXPGt")
        s3secretkey = os.environ.get("S3SecretKey", "RSSEQXXXXXX26sJAzL4uW")
        client = Minio(
            s3url,
            access_key=s3accesskey, # hier natürliuch os.env
            secret_key=s3secretkey, # hier auch
            secure=True
        )
        cmd = sys.argv[1]
        print(cmd)
        if cmd == "read":
            Read(client, sys.argv[2])
        elif cmd == "upload":
         CreateAndUpload(client, sys.argv[2])
        else:
            print("cmd not found.")
    except S3Error as exc:
        print("error occurred.", exc)