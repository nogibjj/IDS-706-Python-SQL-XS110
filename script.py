import polars as pl
import matplotlib.pyplot as plt


def readfile(file_path):
    data = pl.read_csv(file_path)
    return data


def descript_stat(df):

    # Head 5 rows
    print("=== Dataset Overview ===")
    print(df.head())
    print("\n")

    # Summary statistics using the describe method
    summary_stats = df.describe()
    print("=== Descriptive Statistics Overview ===")
    print(summary_stats)
    print("\n")

    # Mean, Median and Mode
    print("=== Mean, Median and Mode Overview ===")
    mean = df.mean()
    median = df.median()
    print("Mean:\n", mean)
    print("Median:\n", median)
    print("\n")

    # Variance and standard deviation
    variance = df.var()
    std_deviation = df.std()
    print("=== Variance and standard deviation Overview ===")
    print("Variance:\n", variance)
    print("Standard Deviation:\n", std_deviation)


def save_report(data, output_summary_report, histogram_image_path, boxplot_image_path):
    # Generate summary statistics for numeric columns
    summary_stats = data.describe()

    # Create a histogram visualization for the '2022 Population' column
    plt.hist(data[["2022 Population"]], bins=20, color="blue", alpha=0.7)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of 2022 Population")
    plt.savefig(histogram_image_path, bbox_inches="tight")
    plt.close()

    # Create a boxplot visualization for the '2022 Population' column
    plt.boxplot(data[["2022 Population"]])
    plt.xlabel("2022")
    plt.ylabel("2022 Population")
    plt.title("Boxplot of 2022 Population")
    plt.savefig(boxplot_image_path, bbox_inches="tight")
    plt.close()

    # Save the summary report in Markdown format
    with open(output_summary_report, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(summary_stats.to_pandas().to_markdown())
        markdown_file.write(f"\n![Histogram]({histogram_image_path})\n")
        markdown_file.write(f"\n![Boxplot]({boxplot_image_path})\n")
    print(f"Summary report saved to {output_summary_report}")
