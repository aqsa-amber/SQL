# FAST SQL – The AI SQL Copilot for Analysts & Teams

**Write complex queries. No SQL required.**

---

## Overview

FAST SQL is an AI-powered SQL generator designed for analysts, business teams, and anyone who needs fast, accurate access to data—without writing SQL. Just describe your data needs in plain English, specify your database, tables, and columns, and QueryGenie instantly generates optimized SQL queries.

---

## Features

- 🧠 **AI-Powered SQL Generation:** Converts natural language requests into SQL queries.
- 📝 **User-Friendly Interface:** Simple Streamlit web app for inputting database, table, and column details.
- ⚡ **Instant Results:** Get full SQL queries in seconds.
- 🔒 **No SQL Knowledge Required:** Designed for both technical and non-technical users.
- 🏢 **Supports Filters, Joins, Aggregations:** Handles complex query logic with ease.

---

## Demo

1. **Input** your database name, table, and columns.
2. **Describe** the action you want (e.g., "Show average sales by region for Q1").
3. **Generate** and copy your SQL query instantly.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/techwatt/sql-generator.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd sql-generator
   ```
3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Start the Streamlit app:
```bash
streamlit run main.py
```
Open the provided local URL in your browser and follow the on-screen instructions.

---

## Project Structure

- `main.py` – Streamlit app and UI logic
- `configs/config.py` – API KEY  configuration
- `model/llm_setup.py` – Language model setup
- `prompts/prompts.py` – Prompt templates for SQL generation
- `pyproject.toml` – Python dependencies
- `uv.lock` – Python dependencies versions
- `README.md` – Project documentation

---

## Target Users

- Data Analysts, Business Analysts, Product Teams
- Non-SQL users who need data access
- Enterprises in Finance, Healthcare, SaaS, Retail

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

---

## License

This project is licensed under the MIT License.