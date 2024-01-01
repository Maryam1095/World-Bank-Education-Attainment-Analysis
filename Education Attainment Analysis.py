# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:49:02 2024

@author: USER
"""

import pandas as pd

# Read the CSV file into a DataFrame
data_education = pd.read_csv("EDUCATION_ATTAINMENT.csv")

# Display the first few rows using head() and information about the dataset using info()
data_education_head = data_education.head()  # Changed 'data' to 'data_education'
data_education_information = data_education.info()

# Check for missing values in the dataset
data_education_missing_values = data_education.isnull().sum()

# Calculate summary statistics for numerical columns using describe()
data_education_statistics = data_education.describe()

#SECTION 2 : YDATA PROFILING

from ydata_profiling import ProfileReport
import pandas as pd

# Load the dataset into a pandas DataFrame
data_education = pd.read_csv("EDUCATION_ATTAINMENT.csv")

# Generate the profile report using ydata-profiling
profile_1 = ProfileReport(data_education, dark_mode=True, title='Education Attainment Profiling Report')
profile_1.to_widgets()  # Display the report as widgets

# Save the report as an HTML file
profile_1.to_file(output_file="education_attainment_ydata_report.html")
