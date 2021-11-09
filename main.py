import os
from json_schema import generate_schema

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, 'data')
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema')

generate_schema(os.path.join(DATA_PATH, 'data_1.json'), os.path.join(SCHEMA_PATH, 'schema_1.json'))
generate_schema(os.path.join(DATA_PATH, 'data_2.json'), os.path.join(SCHEMA_PATH, 'schema_2.json'))
