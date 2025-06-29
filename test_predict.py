from src.pipeline.predict_pipeline import PredictPipeline, CustomData
import pandas as pd

# Test the prediction pipeline
print("Testing prediction pipeline...")

pipeline = PredictPipeline()

# Create sample data
sample_data = CustomData(
    gender='male',
    race_ethnicity='group A',
    parental_level_of_education='some college',
    lunch='standard',
    test_preparation_course='completed',
    reading_score=72,
    writing_score=74
)

# Convert to dataframe
df = sample_data.get_data_as_data_frame()
print('Sample data created:')
print(df)

# Make prediction
try:
    prediction = pipeline.predict(df)
    print(f'Prediction successful: {prediction}')
except Exception as e:
    print(f'Error during prediction: {e}')
    import traceback
    traceback.print_exc()
