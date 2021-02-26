import os
import shutil
import deploy_job


class SetSecret(deploy_job.DeployJob):
    """ Copy the secret file to the specific direcotry """

    def run(self):
        # copy secret config file
        # this file contains sensitive setting values, keeping out from git repo
        shutil.copy(self.app_config["secret_src"], self.app_config["secret_dest"])
        print("Copying file: %s" % self.app_config["secret_dest"])

    def __init__(self, app_config):
        super(SetSecret, self).__init__(app_config)
        self.app_config["secret_src"] = os.path.join(self.app_config["env_dir"], self.app_config["secret_name"])
        self.app_config["secret_dest"] = os.path.join(self.app_config["code_path"], self.app_config["app_name"],
                                                      self.app_config["secrets_dir_name"],
                                                      self.app_config["secret_name"])
