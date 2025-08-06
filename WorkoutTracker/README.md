# OPEN AI's GPT3 AI Model:
**Acts as a bridge between human communication and computer understanding by combining
computational linguistics, statistical methods, and advanced machine learning, particularly
deep learning, to process language data and perform tasks like translation, sentiment analysis,
and chatbot interactions**

- a smart Natural Language Processing (NLP) model
- can understand, interpret, and generate human language in both text and speech 

### How NLP Model works:
1. User types in a question or command in natural language
2. The model then searches through all of the text and finds you relevant information
_____________________________________________________________________________________________


# Project: Workout Tracking Using Google Sheets
- User Prompt: Tell me what exercises you did: "I ran 2 miles and did 100 jumping jacks"
  - hit enter and the information goes into a spreadsheet
- Get Data into spreadsheet on google sheets
  - Use the Nutritionix API to get Date, Time, Exercise, Duration, and Calories into the spreadsheet

### Step-1: Setup API Credentials and Google Spreadsheet
1. Go to this link and create a copy of the My Workouts Spreadsheet. You may need to login/register
  - link: https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?gid=0#gid=0
  - or create your own sheet if you like
2. Go to the Nutritionix API website and select "Get Your API Key" to sign up for a free account
  - Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email
  - Once logged in, you should be able to access your API key and App id
3. Create a new project in PyCharm and in the main.py 
  - create 2 constants to store the APP_ID and API_KEY that you got from Nutritionix

### Step-2: Get Exercise Stats with Natural Language Queries
1. Using the Nutritionix API Guide, figure out how to print the exercise stats for plain text input
   - You can hard code the API key and the App Id for now
   - Understand Request Headers: https://docx.syndigo.com/developers/docs/understand-request-headers
   - Natural Language for Exercise: https://docx.syndigo.com/developers/docs/natural-language-for-exercise
   - Exercise Parameters: https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

### Step-3: Setup Your Google Sheet with Sheety
1. Log into Sheety with your Google Account: https://sheety.co/
    - use the same account that owns the Google Sheet you copied in step 1
    - Make sure you give Sheety permission to access your Google sheets(if missed log out and log in again)
    - Make sure the email matches between your Google Sheet and Sheety Account
    - Under your Google Account Security settings, double-check that you see Sheety listed as an authorized app
      - Otherwise, your Python code can't access your spreadsheet
2. Create a new project in Sheety with the name "Workout Tracking"
   - paste in the URL of your own "My Workouts" Google Sheet
3. Click on the workouts API endpoint and enable GET and POST

### Step-4: Save Data into Google Sheets
1. Using the Sheety Documentation: https://sheety.co/docs/requests
   - Write some code to use the Sheety API to generate a new row of data in your Google Sheet
   - There should be a row for each of the exercises that you get back from the Nutritionix API
   - The date and time columns should contain the current date and time from the Python datetime module

### Step-5: Authenticate Your Sheety API
1. Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it

### Step-6: Remove hard coded secrets(passwords, API keys, endpoints) and move them into environment variables
   - this process will be slightly different depending on what your environment is
   - update your code to use environment variables for all sensitive data
   - You'll need to import the os module
   - In PyCharm, you can add your environment variables under "Edit Configurations".
   - If you click on the little symbol to the right under "Environment Variables, 
     - you will bring up a window where you can add the key-value pairs one by one
      - you can also copy-paste all the environment variables at the same time
