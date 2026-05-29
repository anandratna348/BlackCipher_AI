MITRE_MAP = {
    "Exploits": {
        "technique": "T1190",
        "name": "Exploit Public-Facing Application",
        "severity": "High"
    },

    "DoS": {
        "technique": "T1499",
        "name": "Endpoint Denial of Service",
        "severity": "Critical"
    },

    "Reconnaissance": {
        "technique": "TA0043",
        "name": "Reconnaissance",
        "severity": "Medium"
    },

    "Fuzzers": {
        "technique": "T1595",
        "name": "Active Scanning",
        "severity": "Medium"
    },

    "Backdoor": {
        "technique": "T1059",
        "name": "Command Execution",
        "severity": "Critical"
    },

    "Shellcode": {
        "technique": "T1203",
        "name": "Exploitation for Client Execution",
        "severity": "Critical"
    },

    "Worms": {
        "technique": "T1105",
        "name": "Ingress Tool Transfer",
        "severity": "High"
    },

    "Generic": {
        "technique": "Unknown",
        "name": "Unknown Threat",
        "severity": "Medium"
    },

    "Normal": {
        "technique": "None",
        "name": "Benign Traffic",
        "severity": "Low"
    }
}


def get_mitre_mapping(
    attack_type: str
):

    return MITRE_MAP.get(
        attack_type,
        MITRE_MAP["Generic"]
    )