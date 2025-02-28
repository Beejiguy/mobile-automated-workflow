import json

def get_sarif_structure():
    sarif_data = {
        "version": "2.1.0",
        "runs": [
        {
        "tool": {
            "driver": {
            "name": "MobReaper - Custom Security Scanner",
            "version": "2.14.1",
            "informationUri": "https://codeql.github.com",
            "rules": [          
            ]
          }
        },
        "results": [       
        ]
      }
     ]
    }
    return sarif_data

def build_output(rules, vulnerabilities):    
    sarif_base = get_sarif_structure()

    sarif_base['runs'][0]['tool']['rules'] = rules
    sarif_base['runs'][0]['results'] = vulnerabilities

    print(json.dumps(sarif_base, indent=4))