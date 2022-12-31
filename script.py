#Initial Variables:
#Age
age = 28
#Gender Identity
gender_identity = 0
#Smoker 
smoker = 0
#Number of Children
num_of_children = 3
#Body Mass Index (BMI)
bmi = 26.2

# Insurance Formula
insurance_cost = 250 * age - 128 * gender_identity +370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Print out of insurance cost
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Adding 4 years
age += 4
# Calculate new insurance cost
new_insurance_cost = 250 * age -128 * gender_identity + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Change between new and old insurance costs
change_in_insurance_cost = new_insurance_cost -insurance_cost

# BMI Factor
# Rewrite age to old age 
age = 28
# Add 3.1 to the BMI
bmi += 3.1
# Calculate new insurance cost
new_insurance_cost = 250 * age - 128 * gender_identity + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Change between new and old insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Gender Identity Factor
# Change gender identity variable
# Calculate new insurance cost
# Change between new and old insurance cost

