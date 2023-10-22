import pandas as pd

input_file_path = "input-permit-data.csv"
output_file_path = "filtered-data.csv"

date_threshold = input("Enter the date threshold (will filter out everything before this) in MM-DD-YYYY format (eg 01-01-2023): ")

df = pd.read_csv(input_file_path)

df["Filing Date"] = pd.to_datetime(df['Filing Date'], format='mixed')

filtered_df = df[df["Filing Date"] > pd.to_datetime(date_threshold, format='%m-%d-%Y')]

filtered_df.to_csv(output_file_path, index=False)

print("Filtered data has been exported to filtered-data.csv")
