from fastapi import APIRouter
from adci_botdetector import BotDetector

router = APIRouter()
detector = BotDetector("app/model.pkl")

@router.get("/")
def predict_from_body():
    features = {
        "avg_key_hold_time_ms": 140.2,
        "avg_interkey_latency_ms": 67.3,
        "typing_duration_ms": 3300.0,
        "avg_mouse_speed": 12.5,
        "max_mouse_speed": 30.0,
        "avg_mouse_accel": 0.85,
        "mouse_movements": 210,
        "keystrokes": 75,
        "paste_detected": 0,
        "hover_count": 18,
        "scroll_count": 12,
        "focus_events": 3,
        "click_count": 22,
        "session_duration": 42            
    }

    feature_list = [
        features["avg_key_hold_time_ms"],
        features["avg_interkey_latency_ms"],
        features["typing_duration_ms"],
        features["avg_mouse_speed"],
        features["max_mouse_speed"],
        features["avg_mouse_accel"],
        features["mouse_movements"],
        features["keystrokes"],
        features["paste_detected"],
        features["hover_count"],
        features["scroll_count"],
        features["focus_events"],
        features["click_count"],
        features["session_duration"]
    ]

    result = detector.predict_from_list(feature_list)
    return {"prediction": result}
