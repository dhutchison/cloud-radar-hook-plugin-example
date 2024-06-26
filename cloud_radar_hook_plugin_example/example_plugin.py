from .template_hooks import get_all_template_hooks
from .resource_hooks import s3_resource_hooks

class ExamplePlugin():

    def get_template_hooks(self) -> list:
        return get_all_template_hooks()

    def get_resource_hooks(self) -> dict:

        return {
            "AWS::S3::Bucket": s3_resource_hooks.hooks()
        }
