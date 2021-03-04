import os
import shutil
import deploy_job


class CleanLib(deploy_job.DeployJob):
    """ Delete the extra files from the specific directory """

    def run(self):
        if not os.path.exists(self.app_config["lib64_path"]):
            raise Exception("Directory not existing: %s" % self.app_config["lib64_path"])
        # list all files and dirs for lib dir
        files = os.listdir(self.app_config["lib64_path"])
        for fn in files:
            # for each file or dir, if not in the list, remove it
            full_path = os.path.join(self.app_config["lib64_path"], fn)
            if fn not in self.app_config["lib_file_dirs"]:
                if os.path.exists(full_path):
                    if os.path.isfile(full_path):
                        os.remove(full_path)
                    if os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                    print("Deleted: %s." % full_path)

    def __init__(self, app_config):
        super(CleanLib, self).__init__(app_config)
        self.app_config["lib64_path"] = os.path.join(self.app_config["code_path"], self.app_config["app_name"],
                                                     self.app_config["default_lib_path"], self.app_config["lib_name"])
