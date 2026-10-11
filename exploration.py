
import random
LOCATIONS = {
    "Hospital": {
        "description": "Search for medical supplies.",
        "danger": "High",
        "encounter_chance": 0.70,
        "supplies": ["Medicine", "First Aid Kit"],
    },
    "Supermarket": {
        "description": "Search for food and water.",
        "danger": "Medium",
        "encounter_chance": 0.40,
        "supplies": ["Food", "Water"],
    },
    "Safehouse": {
        "description": "Search for basic supplies.",
        "danger": "Low",
        "encounter_chance": 0.15,
        "supplies": ["Water", "Blanket"],
    },
}


def explore_location(location_name):
    """Return the result of exploring one location."""

    if location_name not in LOCATIONS:
        raise ValueError("Unknown location")

    location = LOCATIONS[location_name]

    encounter = (
        random.random() < location["encounter_chance"]
    )

    damage = random.randint(10, 25) if encounter else 0
    supply = random.choice(location["supplies"])

    return {
        "location": location_name,
        "encounter": encounter,
        "damage": damage,
        "supply": supply,
    }
