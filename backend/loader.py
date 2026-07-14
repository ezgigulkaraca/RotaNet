import pandas as pd


REQUIRED_COLUMNS = [
    "delivery_id",
    "latitude",
    "longitude",
    "demand"
]


def load_dataset(uploaded_file) -> pd.DataFrame:
    """
    Load and validate a CSV or Excel dataset uploaded
    through Streamlit.

    Parameters
    ----------
    uploaded_file
        Streamlit UploadedFile object.

    Returns
    -------
    pd.DataFrame
        Validated dataset.
    """

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    elif file_name.endswith((".xlsx", ".xls")):

        df = pd.read_excel(uploaded_file)

    else:

        raise ValueError(
            "Unsupported file format. Please upload a CSV or Excel file."
        )

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    df = df.dropna()

    df = df.reset_index(drop=True)

    return df
