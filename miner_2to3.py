# this script is used for converting pulsar miner from python2 compatible to python3 compatible

import os
import glob

### check if conversion has been made by looking for .bak files...
def check_bak_files():
    bakfiles = glob.glob("*.bak")
    if len(bakfiles) > 0: return True
    return False

### perform 2to3 conversion
def _load_scripts():
    with open("miner_scripts_list.txt") as fp:
        script_names = fp.read()
    return script_names.split("\n")[:-1]

def content_convert(script_name):
    "replace tab to 8 spaces... and change python2 to python"
    with open(script_name) as fp:
        script_content = fp.read()

    # change from python2 to python
    script_content = script_content.replace(
        "#!/usr/bin/env python2",
        "#!/usr/bin/env python"
    )

    # change all tab to 8 spaces
    script_content = script_content.replace(
        "\t", "        "
    )

    with open(script_name, "w") as fp:
        fp.write(script_content)

def miner_conversion():
    script_names = _load_scripts()
    for script_name in script_names:
        os.system(f"2to3 -w {script_name}")
        content_convert(script_name)

    if not os.path.exists("./bak"):
        os.makedirs("./bak")

    os.system("mv *.bak ./bak/")

if __name__ == "__main__":
    miner_conversion()

