
import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Brekfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Bolied Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Let's put a pick up list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some Fruits: ", list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)
