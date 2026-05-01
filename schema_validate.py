import argparse
import xmlschema
import pathlib
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "-x",
    "--xml",
    default="schema.xml",
    help="XML schema file to validate with the meta_schema file",
)
args = parser.parse_args()

meta_schema = "meta_schema.xsd"
schema_xml = pathlib.Path(args.xml)
if not schema_xml.exists():
    print(f"Couldn't find schema file {schema_xml}. Aborting...")
    sys.exit(1)

schema = xmlschema.XMLSchema11(meta_schema)
schema.validate(open(schema_xml))

print("Validation Passed")
