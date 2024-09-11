import pandas as pd

class CSVDataCleaner:
    def __init__(self):
        self.file_path = 'Archive/books.csv'
        self.output_file_path = 'Archive/books_cleaned.csv'
        self.link_column = 'title'

    def clean_csv(self):
        try:
            data = pd.read_csv(self.file_path)
            print(f"Data successfully loaded from {self.file_path}.")

            initial_count = len(data)
            data.drop_duplicates(subset=self.link_column, inplace=True)
            cleaned_count = len(data)
            print(f"Removed {initial_count - cleaned_count} duplicates.")

            data.to_csv(self.output_file_path, index=False)
            print(f"Cleaned data saved to {self.output_file_path}.")

        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except Exception as e:
            print(f"Error: {e}")