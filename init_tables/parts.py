"""
TODO
"""

from psycopg2.extensions import cursor
from utils import parse_int


def populate_parts(cur: cursor, rows: list[dict[str, str]]):
    """
    TODO
    """
    for row in rows:
        parts = row['Product'], row['Type'],
        row['Release Date'], parse_int(row['Process Size (nm)']),
        parse_int(row['TDP (W)']), parse_int(row['Transistors (million)']),
        parse_int(row['Freq (MHz)']), row['vendor']
        cur.execute("""
            insert into theme(product, types, release_date, process_size,
            tdp, transistors, frequency, vendor) 
            values(%s, %s, %s, %s, %s, %s, %s, %s) 
            on conflict do nothing
            """, parts)
