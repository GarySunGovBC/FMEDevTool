import os
import deploy_job
import shutil


class Checkout(deploy_job.DeployJob):
    """ Run command lines to check out  """

    @staticmethod
    def rm_dir_exist(fullname):
        fullname = fullname.replace("rmdir", "").replace("/s", "").replace("/q", "").strip()
        return os.path.exists(fullname)

    def __init__(self, app_config):
        super(Checkout, self).__init__(app_config)
        self.token = None
        self.key = None

    def run(self):
        if not self.key:
            raise ValueError("Checkout key not defined.")
        # run defined commands, pull FMETemplate2 and lib64
        for cmd in self.app_config[self.key]:
            cmd_line = cmd
            for param in self.app_config["cmd_param"]:
                cmd_line = cmd_line.replace(param, self.app_config[param])
            if "token_value" in cmd_line and self.token:
                cmd_line = cmd_line.replace("token_value", self.token)
            if cmd_line.startswith('rmdir'):
                if not self.rm_dir_exist(cmd_line):
                    continue
            cmd_line = cmd_line.replace("\\\\", "\\")
            ret = os.system(cmd_line)
            if ret != 0:
                raise Exception("Failed at: %s" % cmd_line)


class CheckoutFME(Checkout):
    """Git checkout for Framework, to specific directory """

    def __init__(self, app_config):
        super(CheckoutFME, self).__init__(app_config)
        self.key = "cmd_bat_fme"
        self.app_config["token_name"] = os.path.join(self.app_config["env_dir"], self.app_config["token_name"])
        self.app_config["output_log_dir"] = os.path.join(self.app_config["code_path"], self.app_config["app_name"],
                                                         self.app_config["default_lib_path"],
                                                         self.app_config["log_dir"])

    def before_run(self):
        f = open(self.app_config["token_name"], "r")
        self.token = f.read()
        f.close()

    def after_run(self):
        if not os.path.exists(self.app_config["output_log_dir"]):
            os.makedirs(self.app_config["output_log_dir"])


class CheckoutLib(Checkout):
    """Git checkout for dependent lib, to specific directory """

    def __init__(self, app_config):
        super(CheckoutLib, self).__init__(app_config)
        self.key = "cmd_bat_lib"
