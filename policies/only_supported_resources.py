from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_check import BaseResourceCheck
from typing import List

#NIFTY_SUPPORTED_TYPES = ['AWS::IAM::Policy', 'AWS::IAM::Group', 'AWS::IAM::User']
NIFTY_SUPPORTED_TYPES = ['AWS::IAM::Policy', 'AWS::IAM::Group', 'AWS::IAM::Role', 'AWS::IAM::User']

class EnforceTags(BaseResourceCheck):

    def __init__(self):
        name = "Ensure only supported resources are deployed"
        id = "NIFTY_2"
        supported_resources = ["*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if conf['Type'] not in NIFTY_SUPPORTED_TYPES:
            return CheckResult.FAILED
        return CheckResult.PASSED

    def get_evaluated_keys(self) -> List[str]:
        return ["Properties/Tags"]

check = EnforceTags()