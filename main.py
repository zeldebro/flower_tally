import os
import pandas as pd
from utils.excel_utils import close_excel, save_to_excel
from utils.question_generator import generate_questions

# Close Excel if it's open
close_excel()

# Create the report folder if it doesn't exist
if not os.path.exists('report'):
    os.makedirs('report')

# Ask the user how many questions they want to generate
num_questions = int(input("How many questions do you want to generate? (up to 1000) "))

# Generate the specified number of questions (up to 1000)
questions = generate_questions(num_questions)

# Combine the questions into a single DataFrame
df = pd.DataFrame(questions)

# Export the DataFrame to an Excel file in the report folder
excel_path = "report/tally_chart_options.xlsx"
save_to_excel(df, excel_path)

print("The tally chart options have been successfully exported to report/tally_chart_options.xlsx.")
