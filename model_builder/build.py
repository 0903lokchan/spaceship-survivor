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
    """Returns a Path object representing the absolute path to the latest available training dataset

    Returns:
        Path: A pathlib.Path object containing the absolute path to the latest dataset
    """
    # TODO search for latest dataset
    latest_dataset_path = cwd.joinpath('dataset/spaceship_titanic_20220628.csv')
    print(f"Latest dataset found: {latest_dataset_path}")
    return latest_dataset_path

def get_export_path(export_dir: str) -> Path:
    """Constructs the absolute path to where the prediction model will be saved.

    Args:
        export_dir (str): Name of the directory to store models.

    Returns:
        Path: A pathlib.Path object containing the absolute path to store the model.
    """
    
    # Construct path to export directory
    dir = cwd.joinpath(export_dir)
    print(f"The model will be exported to {dir}")
    
    # If the directory doesn't exist, create it
    if not dir.exists():
        print(f"Target directory does not exist")
        dir.mkdir(parents=True, exist_ok=False)
        print(f"Directory is created")
        
    # Construct file path using timestamps    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = Path(f"spaceship_survivor_classifier_{timestamp}.joblib")
    return dir.joinpath(filename)

def read_dataset(dataset_path: Path) -> pd.DataFrame:
    """Reads a training dataset with the path supplied.

    Args:
        dataset_path (Path): A pathlib.Path object containing the path to the training dataset.

    Returns:
        pd.DataFrame: A pandas Dataframe object containing training data.
    """
    print(f"Retrieving dataset from {dataset_path}")
    df = pd.read_csv(dataset_path, index_col=index_col)
    print(f"Dataset loaded successfully. A Dataframe of size {df.shape} is created")
    
    # TODO Some essential checks on dataset
    return df

def export_model(model: Pipeline, export_path: Path) -> None:
    """Saves sklearn Pipeline objects into joblib files in order to store prediction models.

    Args:
        model (Pipeline): A sklearn Pipeline object representing prediction models.
        export_path (Path): A pathlib.Path object containing file path to where models are saved.
    """
    print(f"Exporting model to {export_path}")
    joblib.dump(model, export_path)
    print('Model exported successfully')
    
train_data_path = get_latest_dataset_path()
train_df = read_dataset(train_data_path)

# create a trained prediction model from create_model.py
model = make_model(train_df, target_col)

# save the prediction model as a joblib file
export_path = get_export_path(export_dir)
export_model(model, export_path)