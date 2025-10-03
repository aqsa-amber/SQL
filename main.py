from model.llm_setup import llm
from prompts.prompts import sql_prompt
import streamlit as st


# Streamlit app configuration
st.title("🧠 Text to SQL Query Generator")
st.markdown(
    """
    Easily generate SQL queries by providing simple details about your database, table, and the action you want to perform.
    """
)

# Input form for SQL query generation
with st.form("sql_generator_form"):
    st.header("📋 Input Details")

    col1, col2 = st.columns(2)

    with col1:
        database_name = st.text_input("Database Name", placeholder="e.g., customer_db")

    with col2:
        table_name = st.text_input("Table Name", placeholder="e.g., customers")

    columns = st.text_input(
        "Columns (comma-separated)", placeholder="e.g., id, name, age"
    )

    relationships = st.text_area(
        "Table Relationships (JOIN conditions) Optional Field",
        placeholder="e.g., orders.customer_id = customers.id",
    )

    action = st.text_area(
        "Action to Perform",
        placeholder="e.g., Retrieve names of customers older than 30",
    )

    submitted = st.form_submit_button("🚀 Generate SQL Query")


# Handle form submission
if submitted:
    data = [table_name, columns, database_name,  action]
    if not all(data):
        st.warning("⚠️ Please fill in all fields before generating the SQL query.")
        st.stop()

    # Generate SQL query using the language model
    with st.spinner("Generating your SQL query..."):
        sql_query = llm(
            prompt=sql_prompt.format(
                table_name=table_name.split(",") if table_name else [],
                columns=columns.split(",") if columns else [],
                database_name=database_name,
                relationships = relationships.split(',') if relationships else None,
                action=action,
            )
        )

    # Display the generated SQL query
    st.success("✅ SQL Query Generated!")
    if sql_query:
        st.write_stream(sql_query)
    else:
        st.error(
            "❌ Failed to generate SQL query. Please check your inputs and try again."
        )


def main():
    st.run()
if __name__ == "__main__":
    main()

# This code sets up a Streamlit application that allows users to generate SQL queries based on their input.