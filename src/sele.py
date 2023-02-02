import pandas as pd
import yaml

config_path="C:/Users/User/Clase_Big_data/config/config.yml"
config= yaml.safe_load(open(config_path))
df=pd.read_csv(config["file_path"])
print(df)
