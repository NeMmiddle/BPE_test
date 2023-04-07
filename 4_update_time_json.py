import datetime
import json


def change_field_update(data: dict, field: str) -> None:
    if type(data) == dict:
        for key, value in data.items():
            if key == field:
                data[key] = str(datetime.datetime.now())
            change_field_update(value, field)


with open('json_file.json', 'r') as json_file, open('json_file_output.json', 'w') as output_json_file:
    json_load = json.load(json_file)
    change_field_update(json_load, 'updated')
    json.dump(json_load, output_json_file, indent=2)
