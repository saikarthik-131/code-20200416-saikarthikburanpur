
'''1) Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health
risk from Table 1 of the person and add them as 3 new columns'''

# For Faster Processing and to handle large amount of data in efficient manner i'm using Pandas and numpy libraries

import pandas as pd
import numpy as np

print("Select a choice from below")
print("To fetch data from json file press 1")
print("To enter data manually press 2")

choice = int(input("Enter Your Choice : "))

if choice!=1 and choice!=2:
    print("Invalid Choice !! Please select the correct one from given list of options")

if choice==1:
    # Reading json data into a pandas dataframe
    json_filepath = 'C:\POC\data.json'
    data = pd.read_json (json_filepath)

    # Creating a copy of dataframe
    df = pd.DataFrame(data)

    # Function to caluclate BMI using formula BMI(kg/m ) = mass(kg) / height(m)
    def caluclateBMI(data):
        return np.round(data['WeightKg'] / (data['HeightCm'] / 100) ** 2, 1)

    df['BMI'] = df.apply(caluclateBMI, axis=1)

    # Dropping the rows other than BMI
    bmi_df = df
    bmi_df = bmi_df.drop(["Gender","HeightCm","WeightKg"],axis=1)

    # Stores the different ranges of BMI Values
    bmi_range = [
        (bmi_df['BMI'] <= 18.4),
        (bmi_df['BMI'] >= 18.5) & (bmi_df['BMI'] <= 24.9),
        (bmi_df['BMI'] >=  25) & (bmi_df['BMI'] <= 29.9),
        (bmi_df['BMI'] >=  30) & (bmi_df['BMI'] <= 34.9),
        (bmi_df['BMI'] >= 35) & (bmi_df['BMI'] <= 39.9),
        (bmi_df['BMI'] >= 40)
    ]

    # create a list of the values we want to assign for each "bmi_category"
    bmi_category = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese','Severely obese','Very Severely obese']

    # create a list of the values we want to assign for each "health risk category"
    health_risk = ['Malnutrition risk','Low risk','Enhanced risk','Medium risk','High risk','Very High risk']

    #mapping the BMI with respective BMI category and Health Risk
    bmi_df['BMI_Category'] = np.select(bmi_range, bmi_category)
    bmi_df['Health Risk'] = np.select(bmi_range, health_risk)

    # bmi_df has the 3columns which has BMI, BMI Category, Health Risk of each individual person
    print(bmi_df)

    '''2) Count the total number of overweight people using ranges in the column BMI
    Category of Table 1,'''

    Overweight_Count = len(bmi_df[bmi_df['BMI_Category']=='Overweight'])

    print("Count of People who falls under category of OverWeight :",Overweight_Count,sep=" ")



if(choice == 2):
    nentries = int(input("Enter the number of Entries you want to enter : "))
    height = []
    weight = []
    bmi_val=[]

    # Function to caluclate BMI
    def caluclateBMI(height, weight):
        return round(weight / (height / 100) ** 2, 1)

    #Accepting the Entries of Height and Weight from the User
    for i in range(0, nentries):
        print("Enter the %d value of Height(in cms)"%(i+1))
        height.append(float(input()))
        print("Enter the %d value of Weight(in kgs)"%(i+1))
        weight.append(float(input()))
        bmi_val.append(caluclateBMI(height[i], weight[i]))

    BMI_Category = []
    Health_Risk = []

    # Function to check the BMI Range and assign the respective BMI category and Health Risk
    def getHealthStatus(bmi):
        if bmi<=18.4:
            BMI_Category.append("Under Weight")
            Health_Risk.append("MalNutrition Risk")

        elif bmi >= 18.5 and bmi <= 24.9:
            BMI_Category.append("Normal Weight")
            Health_Risk.append("Low Risk")

        elif bmi >= 25 and bmi <= 29.9:
            BMI_Category.append("Overweight")
            Health_Risk.append("Enhanced Risk")

        elif bmi >= 30 and bmi <= 34.9:
            BMI_Category.append("Moderately obese")
            Health_Risk.append("Medium Risk")

        elif bmi >= 35 and bmi <= 39.9:
            BMI_Category.append("Severely obese")
            Health_Risk.append("High Risk")

        elif bmi >= 40:
            BMI_Category.append("Very Severely obese")
            Health_Risk.append("Very High Risk")
        return bmi,BMI_Category[i],Health_Risk[i]

    print(" BMI , BMI_Category , Health_Risk ")
    for i in range(0,len(bmi_val)):
        print(getHealthStatus(bmi_val[i]))

    overweight_count = 0
    # Count of Overweight People Category
    for i in BMI_Category:
        if(i=="Overweight"):
            overweight_count+=1
    print("Count of Overweight persons : %d"%overweight_count)

option = input("Press Any Key to exit")


