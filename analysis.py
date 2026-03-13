import pandas as pd
import matplotlib.pyplot as plt


# distribution des années de sortie
def year_distribution(movies):

    df = pd.DataFrame(movies)

    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    fig, ax = plt.subplots()

    df["year"].plot(
        kind="hist",
        bins=20,
        ax=ax
    )

    ax.set_title("Distribution des années de sortie")

    return fig


# statistiques sur les films
def movie_statistics(movies):

    df = pd.DataFrame(movies)

    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    stats = {
        "Année moyenne": df["year"].mean(),
        "Film le plus ancien": df["year"].min(),
        "Film le plus récent": df["year"].max(),
        "Nombre total de films": len(df)
    }

    return stats