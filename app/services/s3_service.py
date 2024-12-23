import boto3
from botocore.exceptions import NoCredentialsError
from fastapi import UploadFile
from app.core.config import settings

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )

    def upload_file(self, file: UploadFile, bucket_name: str, object_name: str = None) -> str:
        """Upload a file to an S3 bucket

        :param file: File to upload
        :param bucket_name: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: URL of the uploaded file
        """
        if object_name is None:
            object_name = file.filename

        try:
            self.s3_client.upload_fileobj(file.file, bucket_name, object_name)
            file_url = f"https://{bucket_name}.s3.{settings.AWS_REGION}.amazonaws.com/{object_name}"
            return file_url
        except NoCredentialsError:
            raise Exception("Credentials not available") 