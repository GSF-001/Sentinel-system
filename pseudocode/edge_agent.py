def process_signals(signals):
    if detect_fall(signals):
        alert_user()
        send_event("fall_detected")

def detect_fall(signals):
    return signals.accel_spike and signals.no_movement > 60
