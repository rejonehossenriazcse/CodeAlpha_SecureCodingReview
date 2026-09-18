# Secure Coding Review & Vulnerability Audit

This project was developed for **TASK 3: Secure Coding Review** under the **CodeAlpha Cyber Security Internship Program**.

---

## 📌 Project Overview
Static Application Security Testing (SAST) and manual security code auditing are critical phases in the Secure Software Development Life Cycle (SSDLC). This project demonstrates how to identify common vulnerabilities in Python code, analyze their security impact using static analysis, and implement robust remediations adhering to OWASP Top 10 standards.

---

## 🛠️ Tools & Technologies
- **Programming Language:** Python
- **SAST Tool:** `Bandit` (Security linter for Python)
- **Methodology:** Automated Static Code Analysis + Manual Security Hardening

---

## 🔍 Vulnerability Findings & Fixes Summary

| # | Vulnerability Name | Severity | OWASP Risk | Remediation Implemented |
|---|---|---|---|---|
| **1** | Hardcoded Password (`B105`) | Low | A07: Identification & Authentication Failures | Retrieved secrets safely from Environment Variables (`os.getenv`). |
| **2** | SQL Injection (`B608`) | Medium | A03: Injection | Replaced dynamic string formatting with parameterized prepared statements (`?`). |
| **3** | OS Command Injection (`B605`) | High | A03: Injection | Replaced insecure `os.system()` calls with native, non-shell socket connections. |
| **4** | Weak Cryptographic Hash (`B324`) | High | A02: Cryptographic Failures | Upgraded deprecated `MD5` hashing algorithm to modern `SHA-256`. |

---

👤 Author
Name: MD. Rejone Hossen Riaz

Role: Cyber Security Intern

Organization: CodeAlpha

Task: TASK 3 — Secure Coding Review
