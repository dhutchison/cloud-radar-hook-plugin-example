
from cloud_radar.cf.unit import ResourceHookContext


def hooks() -> list:
    return [my_s3_encryption_hook]

# Example hook that verifies  that all S3 bucket definitions
# have the "BucketEncryption" property set
def my_s3_encryption_hook(context: ResourceHookContext) -> None:
    # Use one of the built in functions to confirm the property exists
    context.resource_definition.assert_has_property("BucketEncryption")
