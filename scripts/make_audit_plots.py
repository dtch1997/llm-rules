""" Script to generate plots for result of auditing. 

NOTE: Auditing was done by hand (i.e. pen and paper), so the data is hardcoded here.
"""

from dataclasses import dataclass
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

@dataclass
class AuditResult:
    dataset: str
    true_positive_count: int
    true_negative_count: int
    false_positive_count: int
    false_negative_count: int

    @property 
    def total(self):
        return self.true_positive_count + self.true_negative_count + self.false_positive_count + self.false_negative_count
    
    @property 
    def actual_positive_rate(self):
        """ The fraction of actual positive examples in the dataset. """
        return  (self.true_positive_count + self.false_negative_count) / self.total
    
    @property
    def actual_negative_rate(self):
        return (self.true_negative_count + self.false_positive_count) / self.total

    @property 
    def labelled_positive_rate(self):
        """ The fraction of examples that were labelled as positive. """
        return (self.true_positive_count + self.false_positive_count) / self.total
    
    @property
    def labelled_negative_rate(self):
        return (self.true_negative_count + self.false_negative_count) / self.total
    
    @property
    def false_positive_rate(self):
        if self.false_positive_count == 0:
            return 0
        return self.false_positive_count / (self.false_positive_count + self.true_negative_count)
    
    @property
    def false_negative_rate(self):
        if self.false_negative_count == 0:
            return 0
        return self.false_negative_count / (self.false_negative_count + self.true_positive_count)

results = [
    AuditResult(
        dataset="male_vs_female",
        true_positive_count=7,
        false_negative_count=4,
        false_positive_count=0,
        true_negative_count=9
    ),
    AuditResult(
        dataset="mammal_vs_bird",
        true_positive_count=5,
        false_positive_count=0,
        false_negative_count=5,
        true_negative_count=10,
    ),
    AuditResult(
        dataset="english_vs_french",
        true_positive_count=15,
        false_positive_count=0,
        false_negative_count=3,
        true_negative_count=2,
    ),
    AuditResult(
        dataset="bird_vs_fish",
        true_positive_count=17,
        false_positive_count=0,
        false_negative_count=2,
        true_negative_count=1,
    ),
    AuditResult(
        dataset="german_vs_malay",
        true_positive_count=18,
        false_positive_count=0,
        false_negative_count=1,
        true_negative_count=1,
    ),
    AuditResult(
        dataset="country_vs_not",
        true_positive_count=20,
        false_positive_count=0,
        false_negative_count=0,
        true_negative_count=0,
    ),
]

def make_actual_vs_labelled_accuracy_plot(results: list[AuditResult]):
    rows = []
    for result in results:
        rows.append({
            "dataset": result.dataset,
            "rate": "actual_positive",
            "count": result.actual_positive_rate
        })
        rows.append({
            "dataset": result.dataset,
            "rate": "actual_negative",
            "count": result.actual_negative_rate
        })
        rows.append({
            "dataset": result.dataset,
            "rate": "labelled_positive",
            "count": result.labelled_positive_rate
        })
        rows.append({
            "dataset": result.dataset,
            "rate": "labelled_negative",
            "count": result.labelled_negative_rate
        })
    df = pd.DataFrame(rows)
    plot_df = df[df.rate.isin(["actual_positive", "labelled_positive"])]
    plot_df = plot_df.rename(columns={"rate": "Accuracy", "count": "count"})
    # change the values
    plot_df["Accuracy"] = plot_df["Accuracy"].apply(lambda x: "Judge-Rated" if x == "labelled_positive" else "Human-Rated")

    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_title("Actual vs Labelled Articulation Accuracy ")
    sns.barplot(x="dataset", y="count", hue="Accuracy", data=plot_df, ax=ax)

def make_false_pos_neg_rate_plot(results: list[AuditResult]):
    rows = []
    for result in results:
        rows.append({
            "dataset": result.dataset,
            "type": "false_positive",
            "count": result.false_positive_rate
        })
        rows.append({
            "dataset": result.dataset,
            "type": "false_negative",
            "count": result.false_negative_rate
        })
        rows.append({
            "dataset": result.dataset,
            "type": "false_positive_count",
            "count": result.false_positive_count
        })
        rows.append({
            "dataset": result.dataset,
            "type": "false_negative_count",
            "count": result.false_negative_count
        })

    df = pd.DataFrame(rows)
    plot_df = df[df.type.isin(["false_positive", "false_negative"])]
    # plot_df = df[df.type.isin(["false_positive_count", "false_negative_count"])]
    plot_df = plot_df.rename(columns={"type": "Type", "count": "count"})
    # change the values
    plot_df["Type"] = plot_df["Type"].apply(lambda x: "False Positive" if x == "false_positive" else "False Negative")

    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_title("False Positive and False Negative Rates")
    sns.barplot(x="dataset", y="count", hue="Type", data=plot_df, ax=ax)


if __name__ == "__main__":

    sns.set_theme()
    make_actual_vs_labelled_accuracy_plot(results)
    make_false_pos_neg_rate_plot(results)
