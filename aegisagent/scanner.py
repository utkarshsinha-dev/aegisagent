import subprocess
import json


def run_semgrep():
    result = subprocess.run(
        [
            "semgrep",
            "--config",
            "rules/sql_injection.yml",
            "vulnerability/",
            "--json"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if result.returncode != 0:
        print("Semgrep failed:")
        print(result.stderr)
        return None

    return json.loads(result.stdout)


def extract_findings(data):
    #Take Semgrep's huge JSON and extract only what AegisAgent cares about.
    findings = []

    for result in data.get("results", []):
        finding = {
            "rule": result.get("check_id"),
            "file": result.get("path"),
            "line": result.get("start", {}).get("line"),
            "severity": result.get("extra", {}).get("severity"),
            "message": result.get("extra", {}).get("message")
        }

        findings.append(finding)

    return findings


def main():
    data = run_semgrep()

    if data is None:
        return

    findings = extract_findings(data)

    if not findings:
        print("No vulnerabilities found.")
        return

    print(f"Found {len(findings)} vulnerability/vulnerabilities:\n")

    for finding in findings:
        print(f"Rule:     {finding['rule']}")
        print(f"File:     {finding['file']}")
        print(f"Line:     {finding['line']}")
        print(f"Severity: {finding['severity']}")
        print(f"Message:  {finding['message']}")
        print("-" * 60)


if __name__ == "__main__":
    main()