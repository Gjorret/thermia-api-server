from src.thermia_service import get_heat_pumps, reauthenticate


def set_temperature(temp):
    """Set the heat pump temperature using the Thermia API."""
    try:
        heat_pump = get_heat_pumps()[0]
        heat_pump.set_temperature(temp)
        # If temperature setting is successful, return None (no error)
        return None
    except Exception as e:
        # Return the error message if there's an exception
        return f"Error setting temperature: {str(e)}"
