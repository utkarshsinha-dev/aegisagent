# AegisAgent

**Autonomous Asynchronous Vulnerability Remediation Engine**

> AegisAgent is an evolving security engineering system designed to detect, analyze, remediate, validate, and eventually automate the resolution of software vulnerabilities.

---

## Current Version: v0.0 — Vulnerability Detection Pipeline

The first milestone of AegisAgent establishes the project's **automated vulnerability detection pipeline**.

At this stage, AegisAgent uses **Semgrep** to detect a deliberately introduced SQL injection vulnerability and processes the resulting scan output programmatically through a Python scanner.

### Current Pipeline

```text
Vulnerable Source Code
        ↓
     Semgrep
        ↓
  JSON Scan Output
        ↓
   scanner.py
        ↓
Structured Vulnerability Finding
```

---

## What Has Been Implemented

### 1. Vulnerable Demo Application

A deliberately vulnerable Python function was created to simulate a SQL injection vulnerability.

```python
def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query
```

The vulnerability provides a controlled target for testing AegisAgent's security analysis pipeline.

### 2. Semgrep Detection

A Semgrep rule was created to identify the demonstrated SQL injection pattern.

Semgrep successfully detects the vulnerability and reports information including:

* Rule ID
* File path
* Line number
* Severity
* Vulnerability description

### 3. Automated Scanner

The `scanner.py` module now controls the Semgrep execution programmatically.

Instead of manually running Semgrep and inspecting its output, AegisAgent:

1. Executes Semgrep.
2. Requests JSON output.
3. Parses the returned JSON.
4. Extracts the relevant vulnerability information.
5. Produces a structured finding.

Example:

```text
Found 1 vulnerability/vulnerabilities:

Rule:     rules.python-sql-injection-demo
File:     vulnerability\database.py
Line:     2
Severity: ERROR
Message:  Potential SQL injection: user input is concatenated into a SQL query.
```

---

## Current Architecture

```text
┌─────────────────────────────┐
│     Vulnerable Repository   │
│                             │
│     database.py             │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│           Semgrep           │
│                             │
│   Static vulnerability      │
│        detection            │
└──────────────┬──────────────┘
               │
               │ JSON
               ▼
┌─────────────────────────────┐
│         scanner.py          │
│                             │
│  • Execute Semgrep          │
│  • Parse JSON               │
│  • Extract findings         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Structured Finding        │
│                             │
│   Rule                      │
│   File                      │
│   Line                      │
│   Severity                  │
│   Message                   │
└─────────────────────────────┘
```
---

## Development Philosophy

AegisAgent is being developed as a learning-driven engineering project rather than as a single large AI application.

Each major capability is introduced only after its underlying problem and architecture are understood.

The development progression is:

```text
Detection
   ↓
AI Remediation
   ↓
Patch Application
   ↓
Validation
   ↓
Agentic Control Loop
   ↓
Sandboxing
   ↓
Asynchronous Processing
   ↓
Evaluation & Regression
   ↓
Production Hardening
```

---

## Repository Structure

```text
aegisagent/
│
├── aegisagent/
│   └── scanner.py
│
├── vulnerability/
│   └── database.py
│
├── rules/
│   └── sql_injection.yml
│
└── README.md
```

> The repository structure will evolve as additional components are introduced.

---

## Version History

### v0.0 — Vulnerability Detection Pipeline

* Added deliberately vulnerable SQL injection example.
* Integrated Semgrep for static vulnerability detection.
* Added custom Semgrep detection rule.
* Added programmatic Semgrep execution through `scanner.py`.
* Added JSON parsing and structured vulnerability extraction.
* Established the first AegisAgent detection pipeline.

