import os
import shutil
import deploy_job
import re


class SetUser(deploy_job.DeployJob):
    """ Copy the user config file to the specific direcotry """

    def run(self):
        text = ""
        for s in self.app_config["customize_users"]:
            text += "\"%s\"," % s
        if text:
            text = text[:-1]
        text = "{\n\t\"customize_users\":[%s]\n}" % text
        f = open(self.app_config["user_env_dest"], "w")
        f.write(text)
        f.close()
        print("Creating file: %s" % self.app_config["user_env_dest"])

    def __init__(self, app_config):
        super(SetUser, self).__init__(app_config)
        self.app_config["user_env_dest"] = os.path.join(self.app_config["code_path"], self.app_config["app_name"],
                                                        self.app_config["app_config_dir"], self.app_config["user_env"])
