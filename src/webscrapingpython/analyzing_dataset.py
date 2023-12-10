import pandas as pd
import matplotlib.pyplot as plt


class StaffDataAnalyzer:
    """
    StaffDataAnalyzer class for analyzing and visualizing staff data.

    Attributes:
        scrapedData (list): List of dictionaries containing scraped staff data.
        df (pd.DataFrame): DataFrame to store the scraped data.

    Methods:
        __init__(self, scraped_data: list):
            Initializes a StaffDataAnalyzer instance with scraped data.

        convert_to_dataframe(self) -> pd.DataFrame:
            Converts the list of dictionaries to a DataFrame.

        display_dataframe(self) -> None:
            Displays the DataFrame.

        plot_roles_distribution(self) -> None:
            Plots a bar chart for the distribution of staff titles.
    """

    def __init__(self, scraped_data: list):
        """
        Initializes a StaffDataAnalyzer instance with scraped data.

        Args:
            scraped_data (list): List of dictionaries containing scraped staff data.
        """
        self.scrapedData = scraped_data
        self.df = None

    def convert_to_dataframe(self) -> pd.DataFrame:
        """
        Converts the list of dictionaries to a DataFrame.

        Returns:
            pd.DataFrame: The DataFrame containing the scraped data.
        """
        df = pd.DataFrame(self.scrapedData)
        return df

    def display_dataframe(self) -> None:
        """Displays the DataFrame."""
        if self.df is not None:
            print(self.df)
        else:
            print("DataFrame is not available. Please convert the data first.")

    def plot_roles_distribution(self) -> None:
        """Plots a bar chart for the distribution of staff titles."""
        if self.df is not None and "title" in self.df.columns:
            roles_distribution = self.df["title"].value_counts()
            plt.figure(figsize=(10, 6))
            roles_distribution.plot(kind="bar", color="blue")
            plt.title("Distribution of Staff Titles")
            plt.xlabel("Staff Title")
            plt.ylabel("Count")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
        else:
            print(
                "DataFrame or 'title' column is not available. Please convert the data first."
            )
