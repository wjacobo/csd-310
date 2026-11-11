
"""Module 5.2 - Test the MySQL movies database connection."""

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values
from pathlib import Path

# Read database login information from the .env file.
env_path = Path(__file__).resolve().parent / ".env"
secrets = dotenv_values(env_path)

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

db = None

try:
    # Connect to the MySQL movies database.
    db = mysql.connector.connect(**config)

    print(
        "\nDatabase user {} connected to MySQL on host {} with database {}".format(
            config["user"], config["host"], config["database"]
        )
    )

    input("\nPress Enter to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

finally:
    if db is not None and db.is_connected():
        db.close()
