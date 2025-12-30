from zenml import step

@step
def alert_system(avg_aqi: float, category: str):
    """
    Simple alert system based on AQI.
    """
    if avg_aqi > 200:
        print(f"⚠️ ALERT! AQI is {avg_aqi:.2f} ({category})")
    else:
        print(f"✅ AQI is OK: {avg_aqi:.2f} ({category})")
