from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for template in sorted((ROOT/'templates').glob('*.template.yaml')):
    kind=template.name.split('.')[0]
    schema=yaml.safe_load((ROOT/'schemas'/f'{kind}.schema.yaml').read_text())
    data=yaml.safe_load(template.read_text())
    found=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(data))
    if found:
        errors.extend([f'{template.name}: {e.message}' for e in found])
if errors:
    print('VALIDATION FAILED')
    print('\n'.join(errors))
    raise SystemExit(1)
print('All template YAML files validated successfully.')
