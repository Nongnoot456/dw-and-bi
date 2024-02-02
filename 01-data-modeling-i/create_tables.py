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
        event_id BIGINT NOT NULL,
        event_type varchar(100) NOT NULL,
        actor_id int,
        repo_id int,
        paylaod_action varchar(100) NOT NULL, -- [None (is 'push'), 'start', 'created', 'published', 'closed']
        payload_push_id BIGINT,
        public boolean NOT NULL,
        created_at varchar(100),
        org_id int,
        event_time timestamp NOT NULL,
        PRIMARY KEY(event_id),
        CONSTRAINT FK_actor FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
        CONSTRAINT FK_repo FOREIGN KEY (repo_id) REFERENCES repo(repo_id),
        CONSTRAINT FK_payload FOREIGN KEY (payload_push_id) REFERENCES payload(push_id),
        CONSTRAINT FK_org FOREIGN KEY (org_id) REFERENCES org(org_id)
    )
"""

table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        actor_id int ,
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
        repo_id int,
        repo_name varchar(50),
        repo_url varchar(100),
        PRIMARY KEY(repo_id)
    )
"""

table_create_org = """
    CREATE TABLE IF NOT EXISTS org (
        org_id int,
        org_login varchar(50),
        org_gravatar_id varchar(50),
        org_url varchar(100),
        org_avatar_urlvarchar(100),
        PRIMARY KEY(org_id)
    )
"""

create_table_queries = [
    table_create_events,
    table_create_actors,
    table_create_repo,
    table_create_org,
    
]
drop_table_queries = [
    table_drop_events,
    table_drop_actors,
    table_drop_repo,
    table_drop_org,
    
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