import csv
from typing import Callable, NamedTuple

from psycopg2.extensions import connection

from theme import populate_themes
from part_categories import populate_part_categories
from sets import populate_sets
from parts import populate_parts
from inventories import populate_inventories
from inventory_parts import populate_inventory_parts
from colors import populate_colors
from inventory_sets import populate_inventory_sets


class PopulateTask(NamedTuple):
    create_table_file_path: str
    data_file_path: str
    populate_fn: Callable[[list[dict[str, str]]], None]


def populate(task: PopulateTask, conn: connection) -> None:
    with conn.cursor() as cur:
        with open(task.create_table_file_path, encoding="utf8") as schema_file:
            cur.execute(schema_file.read())
        print(f"executed schema file {task.create_table_file_path}")
        with open(task.data_file_path, encoding="utf8") as csv_file:
            rows = list(csv.DictReader(csv_file))
            task.populate_fn(cur, rows)
        print(f"processed {task.data_file_path}")


POPULATE_TASKS: list[PopulateTask] = [
    PopulateTask("./schema/theme.sql",
                 "./data/themes.csv", populate_themes),
    PopulateTask("./schema/part_categories.sql",
                 "./data/part_categories.csv", populate_part_categories),
    PopulateTask("./schema/sets.sql",
                 "./data/sets.csv", populate_sets),
    PopulateTask("./schema/parts.sql",
                 "./data/parts.csv", populate_parts),
    PopulateTask("./schema/inventories.sql",
                 "./data/inventories.csv", populate_inventories),
    PopulateTask("./schema/inventory_parts.sql",
                 "./data/inventory_parts.csv", populate_inventory_parts),
    PopulateTask("./schema/colors.sql",
                 "./data/colors.csv", populate_colors),
    PopulateTask("./schema/inventory_sets.sql",
                 "./data/inventory_sets.csv", populate_inventory_sets)
]
