import os
import deploy_job


class Checkout(deploy_job.DeployJob):
    """ Run command lines to check out  """

    @staticmethod
    def rm_dir_exist(fullname):
        fullname = fullname.replace("rmdir", "").replace("/s", "").replace("/q", "").strip()
        return os.path.exists(fullname)

    def run(self):
        # virutal method to override
        raise NotImplementedError()

    def run_cmd(self, config, token):
        # run defined commands, pull FMETemplate2 and lib64
        for cmd in self.app_config[config]:
            cmd_line = cmd
            for param in self.app_config["cmd_param"]:
                cmd_line = cmd_line.replace(param, self.app_config[param])
            if token:
                cmd_line = cmd_line.replace("token_value", token)
            if cmd_line.startswith('rmdir'):
                if not self.rm_dir_exist(cmd_line):
                    continue
            ret = os.system(cmd_line)
            if ret != 0:
                raise Exception("Failed at: %s" % cmd_line)

    def __init__(self, app_config):
        super(Checkout, self).__init__(app_config)


class CheckoutFME(Checkout):
    """Git checkout, to specific directory """

    def run(self):
        f = open(self.app_config["token_name"], "r")
        tk = f.read()
        f.close()
        super(CheckoutFME, self).run_cmd("cmd_bat_fme", tk)

    def __init__(self, app_config):
        super(CheckoutFME, self).__init__(app_config)
        self.app_config["token_name"] = os.path.join(self.app_config["env_dir"], self.app_config["token_name"])


class CheckoutLib(Checkout):
    """Git checkout, to specific directory """

    def run(self):
        super(CheckoutLib, self).run_cmd("cmd_bat_lib", None)

    def __init__(self, app_config):
        super(CheckoutLib, self).__init__(app_config)
