# Secure Coding Review – Python Application

## Environment
- Operating System: Windows
- Programming Language: Python
- Tool: Python Interpreter

## Identified Vulnerabilities

### 1. Hardcoded Credentials
Risk: Credentials exposed in source code  
Impact: Unauthorized access  
Severity: High  

### 2. Plain Text Password Handling
Risk: Password theft  
Impact: Account compromise  
Severity: High  

### 3. Lack of Input Validation
Risk: Improper authentication  
Impact: Security bypass  
Severity: Medium  

## Remediation Steps
- Removed plain-text password usage
- Implemented SHA-256 password hashing
- Improved authentication logic

## Conclusion
Applying secure coding practices significantly reduces security risks
in authentication mechanisms.
