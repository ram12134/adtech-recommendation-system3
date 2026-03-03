import pandas as pd

# Load column structure used during training
def prepare_features(data_dict):

    df = pd.DataFrame([data_dict])

    # Convert categorical → one hot encoding
    df = pd.get_dummies(df)

    # Load training columns
    training_columns = pd.read_pickle("training_columns.pkl")

    # Add missing columns
    for col in training_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep same order
    df = df[training_columns]

    return df