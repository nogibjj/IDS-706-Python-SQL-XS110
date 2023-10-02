import main  # Import your main module
import polars as pl


def test_main():
    """Test main.py"""
    input_file_path = "world_population.csv"  # Update with your dataset file path
    summary_report = "report.md"
    histogram_image = "image/population_histogram.png"
    boxplot_image = "image/population_boxplot.png"

    # Read the dataset using pandas
    data = pl.read_csv(input_file_path)

    # Call the function from main.py with the DataFrame
    main.save_report(data, summary_report, histogram_image, boxplot_image)


if __name__ == "__main__":
    test_main()
