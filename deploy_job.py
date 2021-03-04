import sys


class DeployJob(object):
    """ Root class of job class """

    def before_run(self):
        pass

    def run(self):
        # virutal method to override
        raise NotImplementedError()

    def after_run(self):
        pass

    def execute(self):
        self.before_run()
        self.run()
        self.after_run()

    def __init__(self, app_config):
        self.app_config = app_config
