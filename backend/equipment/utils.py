import pandas as pd

def analyze_csv(file):
    df = pd.read_csv(file)

    summary = {
        "total_equipment": int(len(df)),
        "avg_flowrate": float(df["Flowrate"].mean()),
        "avg_pressure": float(df["Pressure"].mean()),
        "avg_temperature": float(df["Temperature"].mean()),
        "type_distribution": df["Type"].value_counts().to_dict(),
        "avg_flowrate_by_type": df.groupby("Type")["Flowrate"].mean().to_dict(),
        "avg_pressure_by_type": df.groupby("Type")["Pressure"].mean().to_dict(),
        "avg_temperature_by_type": df.groupby("Type")["Temperature"].mean().to_dict(),
    }

    return summary
