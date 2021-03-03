# FMEDevTool
Tool program for the development of FME Framework
1. Release FME Framework and dependent library from Git servers, Github and Gogs.
2. Specify release the diectories.
3. Specify configuration settings.

# Configuration for app.json
    "lib_name": "lib64", # folder for lib64
    "secrets_dir_name": "secrets", # folder for secrets
    "env_dir": "..\\Env", # folder to server/workstation evn variables
    "app_env": "deploy.json", # file to save the env variables
    "token_name": "token.txt", # token for Gogs
    "secret_name": "templateDefaults.config", # secret data not to disclose
    "script_specific": "scriptSpecific", # folder for scriptSpecific
    # command lines to checkout the repo to server/workstation
    "cmd_bat_fme": [
      "rmdir code_path\\app_name/s/q",
      "git_path clone -b work_branch https://idir-gsun:token_value@gogs.data.gov.bc.ca/daops/FMETemplate2.git code_path\\app_name"
    ],
    "cmd_bat_lib": [
      "rmdir code_path\\app_name\\lib_name/s/q",
      "python_path -m pip install -r code_path\\app_name\\lib_path\\lib\\requirements.txt -t code_path\\app_name\\lib_path\\lib_name"
    ],
