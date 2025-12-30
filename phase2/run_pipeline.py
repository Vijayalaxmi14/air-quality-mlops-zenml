from pipelines.training_pipeline import air_quality_pipeline

if __name__ == "__main__":
    air_quality_pipeline(data_path="data/raw/city_day.csv")
