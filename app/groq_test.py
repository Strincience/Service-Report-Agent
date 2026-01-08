from groq_client import generate_report

dummy_data = {
    "heading": {
        "service_date": "10 Nov 2025",
        "service_theme": "Walking in Faith",
        "start_time": "8:00 AM",
        "venue": "Main Auditorium"
    }
}

print(generate_report(dummy_data))
