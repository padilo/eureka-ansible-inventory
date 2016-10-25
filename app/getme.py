#  -*- coding: utf-8 -*-
import os
import shutil


def _get_me_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_me():
    script_file = "{}/cli.py".format(_get_me_path())
    script_tmp_file = "/tmp/eureka_inventory.py"

    shutil.copyfile(script_file, script_tmp_file)

    os.chmod(script_tmp_file, 0777)

    print(script_tmp_file)
