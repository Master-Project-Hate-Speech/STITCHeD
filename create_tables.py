import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (

        """
        CREATE TABLE dataset (
            dataset_id SERIAL PRIMARY KEY,
            dataset_origin_name VARCHAR(50) NOT NULL,
            dataset_n`ame VARCHAR(50) NOT NULL,
            unique (dataset_origin_name)
        )
        """,
        """ CREATE TABLE schema (
                dataset_id INT PRIMARY KEY,
                labelName VARCHAR(50) NOT NULL,
                FOREIGN KEY (dataset_id)
                REFERENCES dataset (dataset_id)
                )
        """,
        """ CREATE TABLE text (
                dataset_id INT,
                text_id INT,
                source_id INT,
                text TEXT,
                PRIMARY KEY(dataset_id, text_id),
                FOREIGN KEY (dataset_id)
                REFERENCES schema (dataset_id)
                )
        """,
        """ CREATE TABLE label (
                dataset_id INT,
                text_id INT,
                label_name VARCHAR(50),
                label_value VARCHAR(50),
                label_definition TEXT,
                PRIMARY KEY(dataset_id, text_id, label_name),
                FOREIGN KEY (dataset_id, text_id)
                REFERENCES text (dataset_id, text_id)
                )
        """,
        """ CREATE TABLE textSource(
                source_id SERIAL PRIMARY KEY,
                source VARCHAR(10) NOT NULL
        )
        """
        )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()