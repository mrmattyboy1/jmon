

from jmon.steps.checks.base_check import BaseCheck
from jmon.logger import logger


class ResponseCheck(BaseCheck):

    CONFIG_KEY = "response"

    def _execute(self, selenium_instance, element):
        """Check response code"""
        logger.info("Checking response")
        raise NotImplementedError
