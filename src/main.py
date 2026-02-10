import pandas as pd
import logging as log

log.basicConfig(
    level=log.INFO,
    filename="log.log",
    filemode='w',
    format="%(levelname)s - %(asctime)s - %(message)s"
)


class Cleaner:

    def __init__(self, data = None):
        self.file_path = "../data/messy_sales_data.csv"
        self.dataframe = data

    def get_data(self):
        try:
            log.info("=== Getting Started ====")
            self.dataframe = pd.read_csv(self.file_path, on_bad_lines="skip", engine="python")
            log.info("=== Data has fetched ===")
        except Exception as e:
            log.error(str(e))


    def removes_duplicates(self):
        log.info("=== Removing Duplicates ===")
        self.dataframe = self.dataframe.drop_duplicates(subset=['order_id']).copy()


    def handling_missing(self):
        log.info("=== Handling Missing Values ===")
        #  Exchange the Nan with unknown instead of removing the row, because it is an sales data which is require accuracy.
        self.dataframe[['customer_name', 'city']] = self.dataframe[['customer_name', 'city']].fillna('unknown')

        # had taken mean of the age column
        age = self.dataframe['age'].median()
        # Fills the nan with the age
        self.dataframe['age'] = self.dataframe['age'].fillna(age)
        # Validate the age to be realistic
        self.dataframe.loc[(self.dataframe['age'] < 0) | (self.dataframe['age'] > 100), 'age'] = age

        # Amount average
        amount = self.dataframe['amount'].median()
        self.dataframe['amount'] = self.dataframe['amount'].fillna(amount)

        # Here i am converting date into pandas "DateTime" and correcting the format
        self.dataframe['order_date'] = pd.to_datetime(self.dataframe['order_date'], errors='coerce')
        # Taking the median of the 'order_date' column for filling the Nat error
        date = self.dataframe['order_date'].median()
        # Here i am filling the date in place of Nat
        self.dataframe['order_date'] = self.dataframe['order_date'].fillna(date)


    def standardize_gender(self):
        log.info("=== Standardizing Gender ===")
        self.dataframe['gender'] = self.dataframe['gender'].str.strip().str.capitalize().fillna('Unknown')
        self.dataframe['gender'] = self.dataframe['gender'].replace({
            'M':"Male",
            "F":"Female"
        })

    def standardize_status(self):
        log.info("=== Standardizing Status ===")
        self.dataframe['status'] = self.dataframe['status'].str.strip().str.capitalize()
        self.dataframe['status'] = self.dataframe['status'].replace({"Complete":"Completed"})


    def generate_csv(self):
        log.info("=== Generating CSV File ===")
        path = "../data/cleaned_sales_report.csv"
        self.dataframe.to_csv(path, index=False)
        log.info("=== The data is cleaned Successfully ===")


def main():
    c = Cleaner()
    c.get_data()
    c.removes_duplicates()
    c.handling_missing()
    c.standardize_gender()
    c.standardize_status()
    c.generate_csv()
    print()
    print(c.dataframe.to_string())


if __name__ == '__main__':
    main()