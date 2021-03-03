import os
import shutil
import deploy_job
import re


class SetSecret(deploy_job.DeployJob):
    """ Copy the secret file to the specific direcotry """

    @staticmethod
    def set_path(line, name, value):
        # find the work path. replace with the work path
        m = re.search("^" + name + " *:", line)
        if m is None:
            return line
        return name + ":" + value + "\n"

    def run(self):
        self.set_work_path()
        self.copy_secret()

    def set_work_path(self):
        """
         change the work path in "templateDefaults.config" according to the installation path
        """
        work_path = [
            {
                "name": "rootscriptdir",
                "value": os.path.join(self.app_config["code_path"], self.app_config["app_name"])
            },
            {
                "name": "customizescriptdir",
                "value": os.path.join(self.app_config["code_path"], self.app_config["app_name"],
                                      self.app_config["script_specific"])
            }
        ]
        lines = []
        f = open(self.app_config["secret_src"], "r+")
        text = f.readlines()
        for line in text:
            for pth in work_path:
                line = self.set_path(line, pth["name"], pth["value"])
            lines.append(line)
        f.seek(0)
        f.truncate()
        f.writelines(lines)
        f.close()

    def copy_secret(self):
        # copy secret config file
        # this file contains sensitive setting values, keeping out from git repo
        shutil.copy(self.app_config["secret_src"], self.app_config["secret_dest"])
        print("Copying file: %s" % self.app_config["secret_dest"])

    def __init__(self, app_config):
        super(SetSecret, self).__init__(app_config)
        self.app_config["secret_src"] = os.path.join(self.app_config["env_dir"], self.app_config["secret_name"])
        self.app_config["secret_dest"] = os.path.join(self.app_config["code_path"], self.app_config["app_name"],
                                                      self.app_config["lib_path"],
                                                      self.app_config["secrets_dir_name"],
                                                      self.app_config["secret_name"])
