from typing import NewType

import psycopg2


PostgresCursor = NewType("PostgresCursor", psycopg2.extensions.cursor)
PostgresConn = NewType("PostgresConn", psycopg2.extensions.connection)

table_drop_events = "DROP TABLE IF EXISTS events"
table_drop_actors = "DROP TABLE IF EXISTS actors"
table_drop_repo = "DROP TABLE IF EXISTS repo"
table_drop_org = "DROP TABLE IF EXISTS org"

table_create_events = """
    CREATE TABLE IF NOT EXISTS events (
        id text NOT NULL,
        type text,
        actor_id int,
        PRIMARY KEY(id),
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
"""

table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        actor_id int NOT NULL,
        actor_login vachar(50),
        display_login vachar(50),
        actor_gravatar_id vachar(50),
        actor_url vachar(100),
        actor_avatar_url vachar(100),
        PRIMARY KEY(actor_id)
    )
"""

table_create_repo = """
    CREATE TABLE IF NOT EXISTS repo (
        repo_id int NOT NULL,
        repo_name varchar(50) NOT NULL,
        repo_url varchar(100),
        PRIMARY KEY(repo_id)
    )
"""

table_create_org = """
    CREATE TABLE IF NOT EXISTS org (
        org_id int NOT NULL,
        org_login varchar(50),
        org_gravatar_id varchar(50),
        org_url varchar(100),
        org_avatar_urlvarchar(100),
        PRIMARY KEY(org_id)
    )
"""


create_table_queries = [
    table_create_actors,
    table_create_repo,
    table_create_org,
    table_create_events,
]
drop_table_queries = [
    table_create_actors,
    table_create_repo,
    table_create_org,
    table_create_events,
]

def drop_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()