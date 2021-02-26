import sys

class DeployJob(object):
    """ Root class of job class """

    def run(self):
        # virutal method to override
        raise NotImplementedError()

    def __init__(self, app_config):
        self.app_config = app_config
