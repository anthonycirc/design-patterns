from creational.singleton.singleton import Database


def main() -> None:
    db: Database = Database(name="PostgreSQL", port=5432)
    db_other: Database = Database(name="MySQL", port=3306)

    print(db.__dict__)
    print(db_other.__dict__)

    print(db is db_other)


if __name__ == "__main__":
    main()
