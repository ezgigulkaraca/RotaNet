import pandas as pd
from pathlib import Path


# RotaNet'in ihtiyaç duyduğu zorunlu sütunlar
REQUIRED_COLUMNS = [
    "delivery_id",
    "latitude",
    "longitude",
    "demand"
]


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    CSV veya Excel dosyasını yükler ve doğrular.

    Parameters
    ----------
    file_path : str
        Yüklenecek dosyanın yolu.

    Returns
    -------
    pd.DataFrame
        Temizlenmiş veri seti.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")

    if file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)

    elif file_path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)

    else:
        raise ValueError("Desteklenmeyen dosya formatı. CSV veya Excel kullanın.")

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Eksik sütunlar bulundu: {missing_columns}"
        )

    df = df.dropna()

    df = df.reset_index(drop=True)

    return df
