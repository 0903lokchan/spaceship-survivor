from pathlib import Path
from datetime import datetime
import pandas as pd
from sklearn.pipeline import Pipeline
import joblib

from create_model import make_model

# TODO use proper logging
# TODO add doc
# TODO add error catching

index_col = 'PassengerId'
target_col = 'Transported'
export_dir = 'model'
cwd = Path(__file__).parent

def get_latest_dataset_path() -> Path:
    # TODO search for latest dataset
    latest_dataset_path = cwd.joinpath('dataset/spaceship_titanic_20220628.csv')
    print(f"Latest dataset found: {latest_dataset_path}")
    return latest_dataset_path

def get_export_path(export_dir: str) -> Path:
    dir = cwd.joinpath(export_dir)
    print(f"The model will be exported to {dir}")
    if not dir.exists():
        print(f"Target directory does not exist")
        dir.mkdir(parents=True, exist_ok=False)
        print(f"Directory is created")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = Path(f"spaceship_survivor_classifier_{timestamp}.joblib")
    return dir.joinpath(filename)

def read_dataset(dataset_path: Path) -> pd.DataFrame:
    print(f"Retrieving dataset from {dataset_path}")
    df = pd.read_csv(dataset_path, index_col=index_col)
    print(f"Dataset loaded successfully. A Dataframe of size {df.shape} is created")
    return df

def export_model(model: Pipeline, export_path: Path) -> None:
    print(f"Exporting model to {export_path}")
    joblib.dump(model, export_path)
    print('Model exported successfully')
    
train_data_path = get_latest_dataset_path()
train_df = read_dataset(train_data_path)
model = make_model(train_df, target_col)
export_path = get_export_path(export_dir)
export_model(model, export_path)