def format_output(data):
    """Format the output for display."""
    formatted_data = "\n".join([f"{key}: {value}" for key, value in data.items()])
    return formatted_data

def display_location_on_map(lat, lon):
    """Generate a Google Maps link based on latitude and longitude."""
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=15&size=600x300&key={api_key}"
    return map_url
