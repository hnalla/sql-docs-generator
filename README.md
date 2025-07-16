# SQL Documentation Generator

A utility for developers to generate Markdown documentation from SQL Server (MSSQL) database objects such as views, stored procedures, table-valued functions, and triggers. The generated .md files can be used as knowledge artifacts in tools like ChatGPT's Knowledge or Confluence documentation.

## 🚀 Features

- Extract definitions of:
  - SQL Views
  - Stored Procedures
  - Table-Valued Functions
  - Triggers
- Generate clean, structured Markdown documentation
- Summary tables with links to detailed definitions
- Easy integration with documentation platforms

## 🛠️ Setup

### Install dependencies 
```bash
pip install pandas
```

### Prepare your input CSVs

- procecure defintions.txt (Procedure Name, Procedure Definition)
- xware_views.csv (View Name, View Definition)
- xware_tf.csv (dbo, function_name, function_definition)
- xware_triggers.csv (trigger_name, trigger_definition)

## 📤 Output

The script generates the following Markdown files:

- procedure_definitions_documentation.md
- view_definitions_documentation.md
- table_valued_function_definitions.md
- trigger_definitions_documentation.md

Each file includes:

- Summary table with indexed object names
- SQL definition block for each object

## 🧾 MSSQL Queries to Extract Definitions

Run these queries in SQL Server Management Studio (SSMS) to extract object definitions and save them as CSV or text files.

### 🧮 Stored Procedures
```sql 
SELECT p.name AS [Procedure Name], m.definition AS [Procedure Definition] 
FROM sys.procedures p 
JOIN sys.sql_modules m ON p.object_id = m.object_id;
```

### 🪟 Views
```sql 
SELECT v.name AS [View Name], m.definition AS [View Definition] 
FROM sys.views v 
JOIN sys.sql_modules m ON v.object_id = m.object_id;
```

### 🧩 Table-Valued Functions
```sql 
SELECT o.name AS [Function Name], m.definition AS [Function Definition] 
FROM sys.objects o 
JOIN sys.sql_modules m ON o.object_id = m.object_id 
WHERE o.type = 'TF';
```

### 🧷 Triggers
```sql 
SELECT t.name AS [Trigger Name], m.definition AS [Trigger Definition] 
FROM sys.triggers t 
JOIN sys.sql_modules m ON t.object_id = m.object_id;
```

## ▶️ Usage

Once your CSVs are prepared, run the script:

```bash 
python generate_sql_docs.py
```

The Markdown files will be generated in your working directory.

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues to discuss improvements or new features.

## 📄 License

This project is licensed under the MIT License.