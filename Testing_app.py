import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
streamlit.dataframe(student_dict)

# set index using column
student_df = student_df.set_index('Name')
print(student_df)
