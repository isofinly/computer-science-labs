# json file parser to yml file

import json
import yaml
with open('input.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    with open('output.yml', 'w', encoding="utf8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)