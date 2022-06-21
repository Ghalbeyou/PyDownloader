# Import section
import json
import os
# function install_requirements : install all the requirements
def install_requirements(requires, path):
    os.system(f'pip install -r {requires}')
    os.system(f'py {path}')
    return True
# check if config exists or no
if os.path.isfile('pydl_config.json'):
    # if it exist, load the json and install the requirements.
    with open('pydl_config.json') as config_file:
        config = json.load(config_file)
        install_requirements(config['requirements'], config['main'])
else:
    # if not, use default settings!
    print("config.json file not found")
    print("Doing from defualt config")
    install_requirements('requirements.txt', 'main.py')
    exit()