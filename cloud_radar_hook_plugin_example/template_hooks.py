
from typing import List

from cloud_radar.cf.unit import Template


def get_all_template_hooks() -> list:
    return [
        template_mappings_prefix_checks,
        template_parameters_prefix_checks,
        template_resources_prefix_checks,
        template_outputs_prefix_checks,
    ]

# Example hook that checks that the cloudformation template
# name for all resources starts with an "r".
def template_resources_prefix_checks(template: Template) -> None:
    # Get all the resources
    resources = template.template.get("Resources", {})

    # Check them
    _object_prefix_check(resources, "r")

# Example hook that checks that the cloudformation template
# name for all outputs starts with an "o".
def template_outputs_prefix_checks(template: Template) -> None:
    # Get all the outputs
    outputs = template.template.get("Outputs", {})

    # Check them
    _object_prefix_check(outputs, "o")

# Example hook that checks that the cloudformation template
# name for all mappings starts with an "m".
def template_mappings_prefix_checks(template: Template) -> None:
    # Get all the mappings
    mappings = template.template.get("Mappings", {})

    # Check them
    _object_prefix_check(mappings, "m")

# Example hook that checks that the cloudformation template
# name for all parameters starts with an "r".
def template_parameters_prefix_checks(template: Template) -> None:
    # Get all the parameters
    parameters = template.template.get("Parameters", {})

    # Check them
    _object_prefix_check(parameters, "p")

def _object_prefix_check(items: List[str], expected_prefix: str):
    # Iterate through each parameter checking them
    for item in items:
        if not item.startswith(expected_prefix):
            raise ValueError(
                f"{item} does not follow the convention of starting with '{expected_prefix}'"
            )
