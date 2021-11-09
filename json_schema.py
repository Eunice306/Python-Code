import json


def update(key, _type, obj):
    obj[key] = {
            "type": _type,
            "tag": "",
            "description": "",
            "required": False
        }


def dump_schema(obj, output):
    for k, v in obj.items():
        if isinstance(v, (str,)):
            update(k, "string", output)
        elif isinstance(v, (int,)):
            update(k, "integer", output)
        elif isinstance(v, (list,)):
            update(k, "enum", output)
        else:
            is_json = False
            for sub_k, sub_v in v.items():
                if isinstance(sub_v, (dict,)):
                    is_json = True
                    break
            
            if is_json:
                if k not in output:
                    output[k] = {}
                dump_schema(v, output[k])
            else:
                update(k, "array", output)

    
def generate_schema(input_path, output_path):
    data = {}
    with open(input_path) as fd:
        data = json.load(fd)
    
    result = {'message': {}}
    update("attributes", "array", result)
    dump_schema(data['message'], result['message'])
    
    with open(output_path, 'w') as fd:
        json.dump(result, fd, indent=1)

