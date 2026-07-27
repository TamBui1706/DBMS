import re

with open('DPSuggest.md', 'r', encoding='utf-8') as f:
    text = f.read()

# The content contains pattern sections separated by "---" and starting with "## "
# Let's split by "\n## "
sections = text.split('\n## ')

# Dictionary to hold the extracted blocks
blocks = {}

for sec in sections:
    if "Pattern:" in sec or "Pattern (" in sec or "Pattern" in sec:
        # Get the first line to identify the pattern
        first_line = sec.split('\n')[0].lower()
        if 'singleton' in first_line: blocks['Singleton'] = sec
        elif 'factory method' in first_line: blocks['Factory Method'] = sec
        elif 'builder' in first_line: blocks['Builder'] = sec
        elif 'adapter' in first_line: blocks['Adapter'] = sec
        elif 'facade' in first_line: blocks['Facade'] = sec
        elif 'decorator' in first_line: blocks['Decorator'] = sec
        elif 'composite' in first_line: blocks['Composite'] = sec
        elif 'chain of responsibility' in first_line: blocks['Chain of Responsibility'] = sec
        elif 'observer' in first_line: blocks['Observer'] = sec
        elif 'strategy' in first_line: blocks['Strategy'] = sec
        elif 'command' in first_line: blocks['Command'] = sec
        elif 'template method' in first_line: blocks['Template Method'] = sec

# The 12 patterns to include in order
order = [
    ('Singleton', 'Creational'),
    ('Factory Method', 'Creational'),
    ('Builder', 'Creational'),
    ('Adapter', 'Structural'),
    ('Facade', 'Structural'),
    ('Decorator', 'Structural'),
    ('Composite', 'Structural'),
    ('Chain of Responsibility', 'Behavioral'),
    ('Observer', 'Behavioral'),
    ('Strategy', 'Behavioral'),
    ('Command', 'Behavioral'),
    ('Template Method', 'Behavioral')
]

new_content = """# Design Pattern Analysis: Database Architecture

This document outlines the **12 core Gang of Four (GoF) Design Patterns** applied to the Database Management System (DBMS).

## Summary Table

| Group | Pattern Name | DBMS Use Case |
| :--- | :--- | :--- |
| **Creational** | **1. Singleton** | Ensures core managers like TransactionManager have only one instance. |
| **Creational** | **2. Factory Method** | Centralizes instantiation logic for metadata objects like Indexes. |
| **Creational** | **3. Builder** | Constructs complex Table structures (columns, constraints) step-by-step. |
| **Structural** | **4. Adapter** | Wraps external data sources (CSV/JSON) to implement internal Table interface. |
| **Structural** | **5. Facade** | Provides a simplified `DBMSClient` that hides Parser, Optimizer, and Executor. |
| **Structural** | **6. Decorator** | Dynamically wraps a Table with temporary behaviors (e.g., ReadOnlyDecorator). |
| **Structural** | **7. Composite** | Database contains Schemas, Schema contains Tables, treated uniformly. |
| **Behavioral** | **8. Chain of Responsibility** | Passes permission checks sequentially from Database -> Schema -> Table. |
| **Behavioral** | **9. Observer** | When a row changes, the Table notifies attached Triggers to execute logic. |
| **Behavioral** | **10. Strategy** | Selects Cascade, Restrict, SetNull behavior when deleting rows. |
| **Behavioral** | **11. Command** | `CreateTable`, `DropTable` operations are encapsulated into executable objects. |
| **Behavioral** | **12. Template Method** | `Validate()` defines workflow, constraints only implement `Check()`. |

"""

# Reconstruct the document
idx = 1
for pat, group in order:
    if pat not in blocks:
        print(f"ERROR: Missing block for {pat}")
        exit(1)
        
    sec_content = blocks[pat]
    
    # We need to rewrite the header to match the new numbering
    # Old header: "X. Pattern Name Pattern: Description (Priority)"
    # New header: "## {idx}. {pat} Pattern"
    lines = sec_content.split('\n')
    header_line = lines[0]
    
    # Clean up the rest of the section
    rest_of_body = '\n'.join(lines[1:])
    
    # We might need to keep the "Description (Priority)" part if present
    match = re.search(r'Pattern(?:[:\-])?(.*)', header_line)
    desc = match.group(1).strip() if match else ""
    
    new_header = f"## {idx}. {pat} Pattern: {desc}"
    
    new_content += "\n---\n\n" + new_header + "\n" + rest_of_body + "\n"
    idx += 1

with open('DPSuggest.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully reconstructed DPSuggest.md with 12 patterns.")
