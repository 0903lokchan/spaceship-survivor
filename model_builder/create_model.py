import pandas as pd
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.dummy import DummyClassifier

# TODO use proper logging
# TODO add doc
# TODO add error catching

def prepare_training_data(train_df: pd.DataFrame, target_col: str) -> tuple[pd.DataFrame, pd.Series]:
    train_X = train_df.drop(columns=target_col)
    train_y = train_df[target_col]
    print('Successfully split dataset into feature and label')
    return train_X, train_y  

def create_pipeline() -> Pipeline:
    # TODO this is a dummy model. create 
    pipeline = make_pipeline(DummyClassifier())
    print('Classifier pipeline created')
    return pipeline  

def train_pipeline(pipeline: Pipeline, train_X: pd.DataFrame, train_y: pd.Series) -> Pipeline:
    return pipeline.fit(train_X, train_y)

def make_model(train_df: pd.DataFrame, target_col: str) -> Pipeline:
    train_X, train_y = prepare_training_data(train_df, target_col)
    pipeline = create_pipeline()
    pipeline = train_pipeline(pipeline, train_X, train_y)
    return pipeline
    