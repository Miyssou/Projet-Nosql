import pandas as pd
import matplotlib.pyplot as plt


def age_distribution(users):

    df = pd.DataFrame(users)

    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    fig, ax = plt.subplots()

    df["age"].plot(
        kind="hist",
        bins=10,
        ax=ax
    )

    ax.set_title("Distribution des âges")

    return fig


def age_statistics(users):

    df = pd.DataFrame(users)

    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    stats = {
        "Age moyen": df["age"].mean(),
        "Age minimum": df["age"].min(),
        "Age maximum": df["age"].max(),
        "Nombre utilisateurs": len(df)
    }

    return stats