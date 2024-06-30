# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institute (JJI) is an educational institution established since 2000 with a stellar reputation and many successful graduates. However, a significant challenge faced by the institute is the high number of students who do not complete their education, known as dropouts. This issue not only impacts the institution's reputation but also reduces the number of graduates who can positively contribute to society. To address this problem, Jaya Jaya Institute aims to detect students who may be at risk of dropping out early on. This proactive approach will allow them to provide specialized guidance and necessary support to help these students complete their education.

### Business Problems
Factors Influencing High Dropout Rates at JJI:

The factors contributing to the high dropout rates at JJI are complex due to numerous correlations between influencing variables.
From the 36 variables (excluding Status) and 4424 entries, there are 1421 dropouts out of 3630 (39%), while 794 students are still enrolled.
Several variables show strong correlations with the dropout status:
Curricular_units_2nd_sem_approved
Curricular_units_1st_sem_approved
Curricular_units_2nd_sem_grade
Curricular_units_1st_sem_grade
Tuition_fees_up_to_date
Scholarship_holder
Age_at_enrollment
Application_mode
Debtor
Gender
Course

From data exploration, it was found that course 171 (Animation and Multimedia Design) does not require curricular credits (all values related to curricular activities are zero, and students can still graduate). This is concerning because we cannot analyze dropout factors in terms of academic performance during the academic period.

From these variables, we selected the following after eliminating some variables that has strong correlations with other variables:
Status
Curricular_units_2nd_sem_approved
Curricular_units_2nd_sem_grade
Tuition_fees_up_to_date
Scholarship_holder
Age_at_enrollment
Application_mode
Debtor
Gender
Course
Curricular_units_2nd_sem_enrolled
Mothers_qualification
Admission_grade
Displaced
Curricular_units_2nd_sem_evaluations
Marital_status
Previous_qualification_grade
Mothers_occupation
Curricular_units_2nd_sem_without_evaluations
GDP


Visualization for easier interpretation revealed that dropouts are influenced by economic factors. Dropout students are more likely to:
Have overdue tuition fees
Not hold scholarships
Have mothers working as unskilled workers
Belong to courses such as Management and Nursing
Be debtors, with the majority of debtors experiencing dropout.

Thus, it can be concluded that the dominant factor influencing dropout rates is economic.

A machine learning model was applied to predict dropout probability among enrolled students using dropout and graduate data. The results indicate that 38.5% of enrolled students are at high risk of dropping out. This is a significant concern for JJI, highlighting the need to address the high dropout rate.


### Project Scope
Data Analysis
Undertaking data analysis of student performance datasets provided by Jaya Jaya Institute to uncover factors influencing dropout rates. The analysis employs a comprehensive approach, aiming to identify demographic profiles and overarching trends among dropout groups.

Predictive Modeling
Developing a machine learning model to predict which students are at high risk of dropout based on identified factors.

Dashboard Development
Creating an intuitive dashboard to facilitate real-time monitoring of student performance, enabling Jaya Jaya Institute to gain insights and intervene proactively with students needing additional support.

Implementation and Evaluation
Implementing the predictive model and dashboard, followed by rigorous evaluation to ensure accuracy and effectiveness in identifying at-risk students.

This project aims to empower Jaya Jaya Institute in mitigating dropout rates by leveraging data-driven insights to support student success and strengthen institutional outcomes.

### Preparation

Data Source: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance 
Resources Source: https://github.com/Ngno/JJI/tree/main 

To establish a suitable development environment for this project, ensure you have Python installed. You can set up a virtual environment using Anaconda or pipenv. Here's how you can proceed. You can change the environment name (`env-name`) to your preferred name:

## Setup Environment - Anaconda
```
conda create --name env-name python=3.11.4
conda activate env-name
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
cd path-to-desired-directory

pip install pipenv
python -m venv env-name
.\env-name\Scripts\activate
pip install -r requirements.txt
```
Once activated, your command prompt or terminal should now show the virtual environment name (e.g., (env-name) prefixed to the prompt).

Download the resources.
Ensure all project files are located in the same directory as your environment directory.
You can check the directory by:

## Find Directory - Anaconda
```
conda info --envs
```

## Find Directory - Shell/Terminal:
```
pipenv --venv
```


## Run steamlit app - Dropout Predictor
Once the environment is set up and all project files are located in the same directory, you can proceed to run the Streamlit app using the command:

```
streamlit run dropout_predictor.py
```


## Business Dashboard
The business dashboard is created using Google Looker Studio, accessible here: https://lookerstudio.google.com/s/l190ZzX8fKA


## Running Machine Learning Model
Access the prototype of model here: https://students-dropout-predictor.streamlit.app/
To run the prototype of the machine learning system, follow these steps:

- Enter the values of the student's profile into the provided input fields.
- Click on the 'Predict' button.

The system will process the entered data using the machine learning model.
Finally, you will receive the predicted probability of dropout for the student based on the input profile.

## Conclusion
The project's conclusions reveal significant insights into dropout patterns among students:

The analysis shows that dropout rates are notably higher among students who are their mother's occupation is unskilled worker, is a debtor, no scholarship, and payment not up-to-date. particularly in programs like Management and Nursing. These factors indicating financial challenges. These findings underscore the importance of targeted interventions and support systems to mitigate dropout risks and enhance student retention at Jaya Jaya Institute.

### Recommende Action Items
Action Item 1: Implement Financial Support Programs

- Establish scholarship programs or financial aid initiatives to support students facing financial difficulties, particularly those with overdue tuition fees.
- Collaborate with external sponsors or donors to expand financial assistance opportunities for deserving students.
- Conduct regular financial counseling sessions to educate students and their families about budgeting and financial planning.

Action Item 2: Enhance Academic and Emotional Support Services

- Develop a mentorship program where experienced faculty members or alumni can mentor at-risk students, providing academic guidance and emotional support.
- Offer workshops or seminars on study skills, time management, and stress management to help students cope with academic pressures effectively.
- Create peer support groups or counseling sessions to encourage students to discuss their challenges and seek assistance early.

These action items aim to address both the financial and academic-emotional aspects contributing to dropout rates, fostering a supportive environment that enhances student success and retention.