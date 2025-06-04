from pipeline.extract import get_all_commodity_data
from pipeline.load import load_to_postgres_rds


if __name__ == "__main__":
  data = get_all_commodity_data()
  load_to_postgres_rds(data, schema='public')