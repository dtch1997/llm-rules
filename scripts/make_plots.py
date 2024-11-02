import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

from IPython.display import display, HTML
from llm_rules.utils import RESULTS_DIR

cls_df = pd.read_parquet(RESULTS_DIR / f"icl_cls_gpt-3.5-turbo_200_0.5_summary.parquet.gzip")
art_df = pd.read_parquet(RESULTS_DIR / f"mcq_art_gpt-3.5-turbo_200_0.5_100_summary.parquet.gzip")

# Correlation plot between classification and articulation

df = cls_df.merge(art_df, on=["dataset", "n_icl_examples"], suffixes=("_cls", "_art"))
print(df.columns)
df = df[df.n_icl_examples == 20]
# df = df[df.accuracy_cls >= 0.85]

plt.figure(figsize=(8, 8))
sns.scatterplot(data=df, x="accuracy_cls", y="accuracy_art", hue="dataset")
# Draw the x = y line 
plt.plot([0.5, 1], [0.5, 1], color="black", linestyle="--")