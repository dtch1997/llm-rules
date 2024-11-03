import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

from IPython.display import display, HTML
from llm_rules.utils import RESULTS_DIR

sns.set_theme()

def make_cls_barplot():
    cls_df = pd.read_parquet(RESULTS_DIR / f"icl_cls_gpt-3.5-turbo_200_0.5_summary.parquet.gzip")
    plt.figure(figsize=(10, 8))
    sns.barplot(data=cls_df, y="dataset", x="accuracy", hue="n_icl_examples")
    plt.title("ICL Classification Accuracy")
    plt.xlabel("Dataset")
    plt.ylabel("Accuracy")
    plt.tight_layout()

    plt.axvline(x=0.9, color="black", linestyle="--")

def make_cls_barplot_other():
    cls_df = pd.read_parquet(RESULTS_DIR / f"icl_cls_gpt-3.5-turbo_200_0.5_summary_other.parquet.gzip")
    plt.figure(figsize=(10, 5))
    sns.barplot(data=cls_df, y="dataset", x="accuracy", hue="n_icl_examples")
    plt.title("ICL Classification Accuracy")
    plt.xlabel("Dataset")
    plt.ylabel("Accuracy")
    plt.tight_layout()

    plt.axvline(x=0.9, color="black", linestyle="--")


def make_correlation_plots():
    cls_df = pd.read_parquet(RESULTS_DIR / f"icl_cls_gpt-3.5-turbo_200_0.5_summary.parquet.gzip")
    mcq_art_df = pd.read_parquet(RESULTS_DIR / f"mcq_art_gpt-3.5-turbo_200_0.5_100_summary.parquet.gzip")
    freeform_art_df = pd.read_parquet(RESULTS_DIR / f"freeform_art_gpt-3.5-turbo_200_0.5_100_summary.parquet.gzip")


    # Correlation plot between classification and articulation
    df = cls_df.merge(mcq_art_df, on=["dataset", "n_icl_examples"], suffixes=("_cls", "_mcq_art")).merge(freeform_art_df, on=["dataset", "n_icl_examples"]).rename(columns={"accuracy": "accuracy_freeform_art"})

    print(df.columns)
    df = df[df.n_icl_examples == 20]
    # df = df[df.accuracy_cls >= 0.85]

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="accuracy_cls", y="accuracy_freeform_art", hue="dataset")
    # Draw the x = y line 
    plt.plot([0.5, 1], [0.5, 1], color="black", linestyle="--")
    # Set the legend outside the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title("ICL Classification Accuracy vs. Freeform Articulation Accuracy")
    plt.xlabel("ICL Classification Accuracy")
    plt.ylabel("Freeform Articulation Accuracy")
    plt.tight_layout()

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="accuracy_cls", y="accuracy_mcq_art", hue="dataset")
    # Draw the x = y line 
    plt.plot([0.5, 1], [0.5, 1], color="black", linestyle="--")
    # Set the legend outside the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title("ICL Classification Accuracy vs. MCQ Articulation Accuracy")
    plt.xlabel("ICL Classification Accuracy")
    plt.ylabel("MCQ Articulation Accuracy")
    plt.tight_layout()


    # Plot MCQ articulation accuracy vs. Freeform articulation accuracy
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="accuracy_mcq_art", y="accuracy_freeform_art", hue="dataset")
    # Draw the x = y line
    plt.plot([0.5, 1], [0.5, 1], color="black", linestyle="--")
    # Set the legend outside the plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title("MCQ Articulation Accuracy vs. Freeform Articulation Accuracy")
    plt.xlabel("MCQ Articulation Accuracy")
    plt.ylabel("Freeform Articulation Accuracy")
    plt.tight_layout()

    # Pretty print the dataframe
    print_df = df[["dataset", "accuracy_cls", "accuracy_mcq_art", "accuracy_freeform_art"]]
    print_df.reset_index(drop=True, inplace=True)
    # rename columns
    print_df = print_df.rename(columns={
        "dataset": "Dataset",
        "accuracy_cls": "ICL Classification",
        "accuracy_mcq_art": "MCQ Articulation",
        "accuracy_freeform_art": "Freeform Articulation"
    })
    print(print_df.to_string(index=  False))

if __name__ == "__main__":
    make_cls_barplot()
    make_cls_barplot_other()
    make_correlation_plots()