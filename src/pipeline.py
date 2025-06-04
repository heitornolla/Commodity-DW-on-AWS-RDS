from pipeline.extract import get_all_commodity_data
from pipeline.load import save_to_postgres_rds


if __name__ == "__main__":
  data = get_all_commodity_data()
  save_to_postgres_rds(data, schema='public')