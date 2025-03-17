def calculate_bmi(weight, height):
    height_in_meters = height * 0.0254  # Convert height to meters
    weight_in_kg = weight * 0.453592  # Convert weight to kilograms
    bmi = weight_in_kg / (height_in_meters ** 2)  # Calculate BMI
    return bmi

def bmi_ranges(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:  # Correct boundary condition
        return "Normal weight"
    elif 25 <= bmi < 30:  # Correct boundary condition
        return "Overweight"
    else:
        return "Obese"

def main():
    calculate_again = True
    while calculate_again:
        print("Welcome to the BMI Calculator!")
        
        # Get user input for height
        feet = int(input("Enter your height (feet): "))
        inches = int(input("Enter your height (inches): "))
        height = (feet * 12) + inches  # Convert height to total inches
        
        # Get user input for weight
        weight = float(input("Enter your weight (pounds): "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Determine BMI category
        category = bmi_ranges(bmi)
        
        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
        
        # Ask if the user wants to calculate again
        again = input("Do you want to calculate another BMI? (yes/no): ").strip().lower()
        if again != 'yes':
            calculate_again = False
       
    print("Thank you for using the BMI Calculator!")

if __name__ == "__main__":
    main()