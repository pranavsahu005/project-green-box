import random

def calculate_irrigation_needs(soil_moisture, humidity, forecast_rain):
    """
    Simulates AI-driven irrigation logic for Nexora Plantation.
    """
    base_need = 100 - soil_moisture
    if forecast_rain > 0.5:
        return 0
    
    adjustment = (100 - humidity) * 0.2
    return max(0, base_need + adjustment)

# Simulated sensor data
samples = [calculate_irrigation_needs(random.uniform(20, 80), random.uniform(40, 90), random.random()) for _ in range(100)]
print(f"Mean Irrigation Volume: {sum(samples)/len(samples):.2f}L")
