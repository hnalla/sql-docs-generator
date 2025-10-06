import pandas as pd

# === Load and Clean Data === #

# Load procedure definitions
procedures = pd.read_csv(
    "procedure_definitions.csv",
    header=None,
    names=["Procedure Name", "Procedure Definition"],
)
procedures['Procedure Name'] = procedures['Procedure Name'].str.strip()

# Load view definitions
views = pd.read_csv(
    "view_definitions.csv", header=None, names=["View Name", "View Definition"]
)
views['View Name'] = views['View Name'].str.strip()

# Load table-valued functions
functions = pd.read_csv(
    "function_definitions.csv",
    header=None,
    names=["Function Name", "Function Definition"],
)
functions["Function Name"] = functions["Function Name"].str.strip()

# Load trigger definitions
triggers = pd.read_csv(
    "trigger_definitions.csv", header=None, names=["Trigger Name", "Trigger Definition"]
)
triggers['Trigger Name'] = triggers['Trigger Name'].str.strip()


# === Markdown Generation Utilities === #


def generate_markdown(
    df, title, summary_col, content_col, output_file, section_icon, entity_label
):
    md = [
        f"# {section_icon} {title}\n",
        f"This document provides a reference for all "
        f"{entity_label.lower()}s defined in the system.\n",
        "## 🗂️ Summary Table\n",
        f"| Index | {entity_label} Name |",
        "|-------|----------------------|",
    ]

    for idx, name in enumerate(df[summary_col]):
        md.append(f"| {idx} | `{name}` |")

    md.append(f"\n## 📌 {entity_label} Details\n")
    for idx, row in df.iterrows():
        md.append(f"### {idx + 1}. `{row[summary_col]}`\n")
        md.append("```sql")
        md.append(str(row[content_col]).strip())
        md.append("```\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"✅ Markdown documentation generated: {output_file}")


# === Generate Documentation === #

generate_markdown(
    views,
    "SQL View Definitions Documentation",
    "View Name",
    "View Definition",
    "view_definitions_documentation.md",
    "📄",
    "View"
)

generate_markdown(
    procedures,
    "Stored Procedure Definitions Documentation",
    "Procedure Name",
    "Procedure Definition",
    "procedure_definitions_documentation.md",
    "📄",
    "Procedure"
)

generate_markdown(
    functions,
    "SQL Table-Valued Function (TVF) Definitions Documentation",
    "Function Name",
    "Function Definition",
    "table_valued_function_definitions.md",
    "🧩",
    "Function"
)

generate_markdown(
    triggers,
    "SQL Trigger Definitions Documentation",
    "Trigger Name",
    "Trigger Definition",
    "trigger_definitions_documentation.md",
    "🚀",
    "Trigger"
)
