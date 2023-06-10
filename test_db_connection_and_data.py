import psycopg2

host = "localhost"
port = "5432"
user = "postgres_user"
password = "postgres_password"
database = "my_db"


def test_db_connection():
    try:
        # Connect to the database
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a simple query to test the connection
        cur.execute("SELECT version();")
        result = cur.fetchone()

        # Check that the query returned a result
        assert result is not None

        # Print the version information for the Postgres server
        print("PostgreSQL server version:", result)

        # Close the cursor and database connection
        cur.close()
        conn.close()

    except Exception as e:
        print("Error testing database connection:", e)
        assert False


def test_that_my_db_in_postgres():
    try:
        # Connect to the database
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a simple query to test the connection
        cur.execute("SELECT datname FROM pg_database;")
        result = cur.fetchall()

        # Check that the query returned a result
        assert "my_db" in str(result)

        # Close the cursor and database connection
        cur.close()
        conn.close()

    except Exception as e:
        print("Error getting a list of databases and making sure my_db is in postgres:", e)
        assert False


def test_table_count():
    try:
        # Connect to the database
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Count the number of rows in each table
        cur.execute("SELECT COUNT(*) FROM users;")
        users_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM device_syncs;")
        device_syncs_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM webapp_pageviews;")
        webapp_pageviews_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM bridge_clinics_to_patients;")
        bridge_clinics_to_patients_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM bridge_clinics_to_professionals;")
        bridge_clinics_to_professionals_count = cur.fetchone()[0]

        # Check that the tables have the expected number of rows
        assert users_count == 5699
        assert device_syncs_count == 504733
        assert webapp_pageviews_count == 5792
        assert bridge_clinics_to_patients_count == 5991
        assert bridge_clinics_to_professionals_count == 113

        # Print the table row counts
        print("users table row count:", users_count)
        print("device_syncs table row count:", device_syncs_count)
        print("webapp_pageviews table row count:", webapp_pageviews_count)
        print("bridge_clinics_to_patients table row count:", bridge_clinics_to_patients_count)
        print("bridge_clinics_to_professionals table row count:", bridge_clinics_to_professionals_count)

        # Close the cursor and database connection
        cur.close()
        conn.close()

    except Exception as e:
        print("Error testing table counts:", e)
        assert False
