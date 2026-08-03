# Database Design

## ClinRx-ICU-CCU Data Structure

## Patient Table

Fields:

- Patient_ID
- Age
- Gender
- Weight
- Height
- Admission_Date
- ICU_Diagnosis

## Medication Table

Fields:

- Drug_ID
- Drug_Name
- Drug_Class
- Indication
- Dose
- Route
- Monitoring

## Laboratory Table

Fields:

- Lab_ID
- Patient_ID
- Test_Name
- Result
- Date

## Vital Signs Table

Fields:

- Vital_ID
- Patient_ID
- Parameter
- Value
- Date_Time

## Intervention Table

Fields:

- Intervention_ID
- Patient_ID
- Problem
- Recommendation
- Outcome
- Pharmacist

## Interaction Table

Fields:

- Drug_A
- Drug_B
- Severity
- Management
