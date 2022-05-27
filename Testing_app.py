import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.setindex('Fruit')
# Put a Pick-up list
streamlit.multiselect("Pick some fruits: " , list (my_fruit_list.index))
# Table Display
streamlit.dataframe(my_fruit_list)

