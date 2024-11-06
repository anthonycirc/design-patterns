import logging
from creational.singleton.singleton import Database

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

def main() -> None:
    db: Database = Database(name="PostgreSQL", port=5432)
    db_other: Database = Database(name="MySQL", port=3306)

    logging.info(db.__dict__)
    logging.info(db_other.__dict__)

    logging.info(db is db_other)


if __name__ == "__main__":
    main()
