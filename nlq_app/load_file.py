import os
import pandas as pd
from sqlalchemy import create_engine
import argparse
import sqlite3

# constants
DATABASE_NM = "customer_complaints_db.sqlite"
TABLE_NM = "customer_complaints"

if os.path.isfile(DATABASE_NM):
    os.remove(DATABASE_NM)

ddl_sql = """CREATE TABLE IF NOT EXISTS "customer_complaints" (
  "index" INTEGER,
  "date_received" TEXT,
  "product" TEXT,
  "sub_product" REAL,
  "issue" TEXT,
  "sub_issue" REAL,
  "consumer_complaint_narrative" TEXT,
  "company_public_response" TEXT,
  "company" TEXT,
  "state" TEXT,
  "zip_code" TEXT,
  "tags" TEXT,
  "consumer_consent_provided" TEXT,
  "submitted_via" TEXT,
  "date_sent_to_company" TEXT,
  "company_response_to_consumer" TEXT,
  "timely_response" INTEGER,
  "consumer_disputed" INTEGER,
  "complaint_id" INTEGER
)"""


class Data:
    def __init__(self, file_name: str, file_path: str, sql_engine: str = "sqlite"):
        self.file_name = file_name
        self.file_path = file_path
        self.sql_engine = sql_engine
        # self.file_ext = self.get_file_type()

    def get_file_type(self) -> str:
        """return a file type

        Returns:
            str: returns type of file
        """
        extension = self.file_name.split(".")[-1]
        allowed_file_types = ["csv"]
        if extension not in allowed_file_types:
            raise ValueError(f"{self.file_name} is not a supported file type")
        return extension

    def read_file(self) -> pd.DataFrame:
        """returns a pandas dataframe

        Returns:
            pdf: pd.DataFrame
        """
        try:
            pdf = pd.read_csv(self.file_path + self.file_name)
            print(f"Total rows: {pdf.count()}")
            return pdf
        except Exception as e:
            print(f"Error reading data {str(e)}")
            raise e

    def create_table(self, tbl_name: str) -> None:
        """create table in database"""
        try:
            df = self.read_file()
            conn = sqlite3.connect(
                DATABASE_NM
            )  # create a database called customer_complaints_db
            cur = conn.cursor()
            cur.execute(ddl_sql)
            conn.commit()
            df.to_sql(
                tbl_name, conn, if_exists="append", index=False
            )  # create table in db
        except Exception as e:
            print(f"Error creating data {str(e)}")
            raise e


# def main(args) -> None:
#     file_nm = args.file_name
#     file_path = args.file_path
#     table_nm = args.table_name
#     data = Data(file_name=file_nm, file_path=file_path)
#     data.create_table(table_nm)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Setup data")
#     parser.add_argument(
#         "file_name",
#         type=str,
#         default="credit_card_complaints.csv",
#         help="data that needs to be setup",
#     )
#     parser.add_argument(
#         "file_path",
#         type=str,
#         default="/Users/sharattadimalla/github/nlq-app/public_data/",
#         help="full path of the file",
#     )
#     parser.add_argument(
#         "table_name",
#         type=str,
#         default="customer_complaints",
#         help="full path of the file",
#     )
#     args = parser.parse_args()
#     main(args)
