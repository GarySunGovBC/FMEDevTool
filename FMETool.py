import os
import sys
import json
import checkout
import clean_lib
import set_secret

CONFIG = "app.json"

app_config = {}
# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
# read settings from env json file, default to "..\Env\deploy.json", for local path and env vars
with open(os.path.join(app_config["env_dir"], app_config["app_env"])) as env_config_json:
    env_config = json.load(env_config_json)
app_config["app_name"] = env_config["app_name"]
app_config["python_path"] = env_config["python_path"]
app_config["git_path"] = env_config["git_path"]
app_config["code_path"] = env_config["code_path"]
app_config["work_branch"] = env_config["work_branch"]
app_config["lib_path"] = env_config["lib_path"]


def class_factory(key):
    """Class factory."""
    # deploy files
    if key == 'checkout_fme':
        return checkout.CheckoutFME(app_config)
    if key == 'checkout_lib':
        return checkout.CheckoutLib(app_config)
    # remove extra dir and file in lib64
    if key == 'clean':
        return clean_lib.CleanLib(app_config)
    # copy secret file
    if key == 'secret':
        return set_secret.SetSecret(app_config)
    return None;


# create jobs in the list
# use command line args to choose jobs to run
for cls in sys.argv:
    job = class_factory(cls)
    if job:
        job.run()
try:
    raw_input("Done. Hit ENTER to close...")
except:
    pass
