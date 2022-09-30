import pandas as pd
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.dummy import DummyClassifier

# TODO use proper logging
# TODO add doc
# TODO add error catching

def prepare_training_data(train_df: pd.DataFrame, target_col: str) -> tuple[pd.DataFrame, pd.Series]:
    """Performs all the preprocessing necessary to the dataset for sklearn pipelines to ingest.

    Args:
        train_df (pd.DataFrame): Training dataset
        target_col (str): Name of the target column

    Returns:
        tuple[pd.DataFrame, pd.Series]: Feature and label sets of training data.
    """
    train_X = train_df.drop(columns=target_col)
    train_y = train_df[target_col]
    print('Successfully split dataset into feature and label')
    return train_X, train_y  

def create_pipeline() -> Pipeline:
    """Creates a sklearn pipeline to be trained.

    Returns:
        Pipeline: A sklearn predictor pipeline with complete archetecture, ready to be trained.
    """
    # TODO this is a dummy model. create 
    pipeline = make_pipeline(DummyClassifier())
    print('Classifier pipeline created')
    return pipeline  

def train_pipeline(pipeline: Pipeline, train_X: pd.DataFrame, train_y: pd.Series) -> Pipeline:
    """Trains a sklearn prediction pipeline with training data.

    Args:
        pipeline (Pipeline): Prediction model to be trained.
        train_X (pd.DataFrame): Feature set of training data.
        train_y (pd.Series): Label set of training data.

    Returns:
        Pipeline: _description_
    """
    return pipeline.fit(train_X, train_y)

def make_model(train_df: pd.DataFrame, target_col: str) -> Pipeline:
    """Creates a prediction model with preset archetecture and given training dataset.

    Args:
        train_df (pd.DataFrame): Training dataset.
        target_col (str): Name of the target column.

    Returns:
        Pipeline: _description_
    """
    train_X, train_y = prepare_training_data(train_df, target_col)
    pipeline = create_pipeline()
    pipeline = train_pipeline(pipeline, train_X, train_y)
    return pipeline
    