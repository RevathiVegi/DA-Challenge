import pandas as pd
import psycopg2


def get_df_from_sql_file(filename_and_path):
    host = "localhost"
    port = "5432"
    user = "postgres_user"
    password = "postgres_password"
    database = "my_db"

    # %% Connect to the database
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute SQL commands from file
    with open(filename_and_path, "r") as f:
        cur.execute(f.read())

    # Fetch results into a pandas dataframe
    columns = [desc[0] for desc in cur.description]
    result_df = pd.DataFrame(cur.fetchall(), columns=columns)

    # Close the cursor and database connection
    cur.close()
    conn.close()

    return result_df


example_df = get_df_from_sql_file(filename_and_path="example_sql_file.sql")

# Print the resulting dataframe
print(example_df)
