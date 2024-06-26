from pathlib import Path

import pytest
from cloud_radar.cf.unit import Template

from cloud_radar_hook_plugin_example.resource_hooks import s3_resource_hooks


@pytest.fixture(autouse=True)
def configure_hooks():
    # Add in locally defined hooks
    Template.Hooks.resources = {
        "AWS::S3::Bucket": s3_resource_hooks.hooks()
    }

    yield

    # Clear the hooks after
    Template.Hooks.resources = {}

# Check the hooks method returns the right number
def test_hooks_count():
    assert 1 == len(s3_resource_hooks.hooks())

def test_bucket_encryption_success():
    template = Template.from_yaml(Path(__file__).parent / "s3_resource_pass.yaml")

    # Render the stack, this will execute the resource level hooks
    template.create_stack(params={"pName": "test"}, region="xx-west-3")

def test_bucket_encryption_failure():

    template = Template.from_yaml(Path(__file__).parent / "s3_bucket_encryption_fail.yaml")

    with pytest.raises(AssertionError, match="Resource 'rS3Bucket' has no property BucketEncryption."):
        # Render the stack, this will execute the resource level hooks
        template.create_stack(params={"pName": "test"}, region="xx-west-3")
