
import boto3
import boto3.session

import jmon.config


class ArtifactStorage:

    def __init__(self):
        """Create client"""
        s3_kwargs = {}
        if endpoint := jmon.config.Config.get().AWS_ENDPOINT:
            s3_kwargs['endpoint_url'] = endpoint
            s3_kwargs['config'] = boto3.session.Config(signature_version='s3v4')
        self._s3 = boto3.client('s3', **s3_kwargs)

    def upload_file(self, path, content=None, source_path=None):
        """Upload log to s3"""
        # If a source path is provided, read content from file
        if source_path:
            with open(source_path, 'rb') as fh:
                content = fh.read()

        self._s3.put_object(
            Bucket=jmon.config.Config.get().AWS_BUCKET_NAME,
            Key=path,
            Body=content
        )
