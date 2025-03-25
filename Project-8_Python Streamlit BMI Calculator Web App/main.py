import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to interpret BMI result
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit App
def main():
    # Title of the app
    st.title("BMI Calculator")

    # Input fields for weight and height
    st.write("Enter your details to calculate your BMI:")

    # Input from user
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (m):", min_value=0.1, step=0.01)

    if st.button("Calculate BMI"):
        # Calculate BMI when button is pressed
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            bmi_category = get_bmi_category(bmi)
            st.write(f"Your BMI is: {bmi:.2f}")
            st.write(f"Category: {bmi_category}")
        else:
            st.error("Please enter valid values for weight and height.")

if __name__ == '__main__':
    main()
