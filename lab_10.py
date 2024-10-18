import streamlit as st

# Function to convert temperatures
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

# Streamlit interface
st.title("Temperature Converter")

# Input values
value = st.number_input("Enter temperature value:")
from_unit = st.selectbox("From unit:", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("To unit:", ["Celsius", "Fahrenheit", "Kelvin"])

if st.button("Convert"):
    result = convert_temperature(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} is {result:.2f} {to_unit}.")
