# Online Fraud Detection Analysis

This report summarizes the analysis performed on the online fraud detection dataset.

## Data Cleaning

- Checked for missing values: No missing values were found in the dataset.
- Checked for duplicates: No duplicate entries were found.

## Data Preprocessing

- **Outlier Removal:** Outliers were identified and removed using the IQR method for the following columns: 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', and 'newbalanceDest'.

- **Categorical Variable Encoding:**
    - Extracted the first letter code from 'nameOrig' and 'nameDest' columns.
    - Dropped the original 'nameOrig' column as all values were the same.
    - Performed one-hot encoding on the 'nameDest_code' column, keeping only the relevant category 'C' associated with fraudulent payments.
    - Analyzed transaction types and found that only 'TRANSFER' and 'CASH_OUT' types had fraudulent cases. Other types were removed, and one-hot encoding was applied to the 'type' column.
    - Removed the 'isFlaggedFraud' column as all values were the same.

- **Data Type Conversion:** Converted 'isFraud' to boolean and 'step' to float.

- **Normalization:** Normalized numerical columns using MinMaxScaler to scale values between 0 and 1.

## Feature Engineering

- Used the Featuretools library to perform automated feature engineering.
- Generated a feature matrix with additional features.

## Addressing Class Imbalance

- Applied RandomUnderSampler to address the class imbalance in the 'isFraud' target variable.
- Verified that the resampled dataset has a balanced distribution of fraud and non-fraud cases.

## Implementing Classification Algorithms

- Split the resampled dataset into training (80%) and testing (20%) sets.
- Trained and evaluated the following classification models:
    - **Logistic Regression**
    - **Random Forest**
    - **XGBoost**

- For each model, generated:
    - Classification report with precision, recall, and F1-score.
    - Confusion matrix to visualize model performance.
    - Precision-Recall curve to assess the trade-off between precision and recall.
    - ROC curve and AUC score to evaluate the model's ability to discriminate between classes.

- XGBoost model had highest score but Random forest was very accurate as well.