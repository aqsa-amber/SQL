from langchain_core.prompts import PromptTemplate

# SQL query generation prompt template
sql_prompt = PromptTemplate(
    input_variables=["table_name", "columns", "database_name","relationships","action"],
    template="""

    You are an expert SQL query generator for a company called TechWatt. Given the following information, generate a SQL query for the user
    based on the {action} they want to perform:

    Table Name: {table_name}
    Columns: {columns}
    Database Name: {database_name}
    Relationships: {relationships}
   

    -Columns: A list of columns to be selected in the SQL query.
    -Table Name: The name of the table from which to select the columns it can be listed.
    -Database Name: The name of the database where the table is located.
    -Relationships: The relationship between two or more tables if any.
    -Action: The action the user wants to perform, such as "retrieve", "insert", "update", or "delete".


    Generate a SQL query that retrieves the specified columns from the table.
    Ensure the query is syntactically correct and optimized for performance.
    Consider relationship between tables if there's more than one table.
    
    Note: Return the SQL query as a string without any additional explanation or comments.
    """
)
