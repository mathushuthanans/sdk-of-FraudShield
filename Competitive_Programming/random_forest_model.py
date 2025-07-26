import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the updated CSV
test_df = pd.read_csv("/home/mathushuthanans/Downloads/training_data_active_bot.csv")

features = ['avg_key_hold_time_ms', 'avg_interkey_latency_ms', 'typing_duration_ms',
            'avg_mouse_speed', 'max_mouse_speed', 'avg_mouse_accel', 'mouse_movements',
            'keystrokes', 'paste_detected', 'hover_count', 'scroll_count', 'focus_events',
            'click_count',  'session_duration', 'mouse_variability']
X = test_df[features]
y = test_df['label']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the retrained model
with open("model_retrained.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model retrained and saved as 'model_retrained.pkl'")

# Predict with the new model
predictions = model.predict(X)
accuracy = (predictions == y).mean()
print(f"Model accuracy: {accuracy:.2%}")

# Compare with variability_prediction
var_pred_accuracy = (test_df['variability_prediction'] == y).mean()
print(f"Variability prediction accuracy: {var_pred_accuracy:.2%}")