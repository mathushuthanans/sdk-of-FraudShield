import pandas as pd

# Read the CSV file
test_df = pd.read_csv("/home/mathushuthanans/Downloads/training_data_active_bot.csv")

# Calculate mouse variability
test_df['mouse_variability'] = test_df[['avg_mouse_speed', 'max_mouse_speed', 'avg_mouse_accel']].std(axis=1)

# Example threshold (tune based on data)
threshold = test_df[test_df['label'] == 0]['mouse_variability'].mean() + test_df[test_df['label'] == 0]['mouse_variability'].std()

test_df['variability_prediction'] = test_df['mouse_variability'].apply(lambda x: 1 if x > threshold else 0)
test_df.to_csv("/home/mathushuthanans/Downloads/training_data_active_bot.csv", index=False)

print(f"Accuracy using variability threshold: {(test_df['variability_prediction'] == test_df['label']).mean():.2%}")