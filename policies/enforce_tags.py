from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_check import BaseResourceCheck
from typing import List

class EnforceTags(BaseResourceCheck):

    def __init__(self):
        name = "Ensure resource has tags"
        id = "NIFTY_1"
        supported_resources = ["*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'Properties' in conf.keys():
            if 'Tags' in conf['Properties'].keys():
                tags = conf['Properties']['Tags']
                if tags:
                    for tag in tags:
                        if tag["Key"] == "iac-platform" and tag["Value"] == "Control Tower Customization":
                            return CheckResult.PASSED
        return CheckResult.FAILED

    def get_evaluated_keys(self) -> List[str]:
        return ["Properties/Tags"]

check = EnforceTags()