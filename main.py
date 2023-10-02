from script import descript_stat
from script import save_report
from script import readfile


def generate_report():
    input_file_path = "world_population.csv"  # Update with your dataset file path
    summary_report = "report.md"
    histogram_image = "image/population_histogram.png"
    boxplot_image = "image/population_boxplot.png"

    WP_data = readfile(input_file_path)

    # country's population in 2022, growth rate and area.
    data = WP_data[["2022 Population", "Growth Rate", "Area (km²)"]]

    descript_stat(data)
    save_report(data, summary_report, histogram_image, boxplot_image)


if __name__ == "__main__":
    generate_report()
