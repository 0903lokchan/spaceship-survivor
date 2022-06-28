from pathlib import Path
from datetime import datetime
import pandas as pd
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.dummy import DummyClassifier
import joblib

# TODO add print messages and loggin
# TODO add doc

index_col = 'PassengerId'
target_col = 'Transported'
export_dir = 'model'
cwd = Path(__file__).parent

def get_latest_dataset() -> Path:
    # TODO search for latest dataset
    return cwd.joinpath('dataset/spaceship_titanic_20220628.csv')

def get_export_path(export_dir: str) -> Path:
    dir = cwd.joinpath(export_dir)
    dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = Path(f"spaceship_survivor_classifier_{timestamp}.joblib")
    return dir.joinpath(filename)

def prepare_training_data(dataset_path: Path) -> tuple[pd.DataFrame, pd.Series]:
    print(f"Retrieving dataset from {dataset_path}")
    df = pd.read_csv(dataset_path, index_col=index_col)
    print(f"Dataset loaded successfully. A Dataframe of size {df.shape} is created")
    train_X = df.drop(columns=target_col)
    train_y = df[target_col]
    print('Successfully split dataset into feature and label')
    return train_X, train_y  

def create_pipeline() -> Pipeline:
    # TODO this is a dummy model. create 
    pipeline = make_pipeline(DummyClassifier())
    print('Classifier pipeline created')
    return pipeline  

def train_pipeline(pipeline: Pipeline, train_X: pd.DataFrame, train_y: pd.Series) -> Pipeline:
    return pipeline.fit(train_X, train_y)

def export_model(model: Pipeline, export_path: Path) -> None:
    print(f"Exporting model to {export_path}")
    joblib.dump(model, export_path)
    print('Model exported successfully')

train_data_path = get_latest_dataset()
train_X, train_y = prepare_training_data(train_data_path)
pipeline = create_pipeline()
pipeline = train_pipeline(pipeline, train_X, train_y)
export_path = get_export_path(export_dir)
export_model(pipeline, export_path)
