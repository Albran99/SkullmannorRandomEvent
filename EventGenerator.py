import json
import random

# Load JSON data from files
def load_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Load events from JSON files
tavern_events = load_json('tavern_events.json')
emmek_actions = load_json('emmek_actions.json')
faction_actions = load_json('faction_actions.json')

def generate_random_event():
    # Randomly select a tavern event and an Emmek Frewn action
    tavern_event = random.choice(tavern_events["events"])
    frewn_action = random.choice(emmek_actions["actions"])

    # Randomly select a faction
    faction = random.choice(list(faction_actions["factions"].keys()))
    print(f"Randomly Selected Faction: {faction}")
    
    # Prompt the user for the reputation level
    while True:
        pc_reputation = input("Enter reputation level (very_high, high, neutral, low, very_low): ").lower()
        if pc_reputation in ["very_high", "high", "neutral", "low", "very_low"]:
            break
        else:
            print("Invalid input. Please enter 'very_high', 'high', 'neutral', 'low', or 'very_low'.")
    
    # Faction interactions based on PC reputation
    faction_reactions = faction_actions["factions"][faction].get(pc_reputation, ["The faction shows no interest in the tavern at this time."])
    faction_reaction = random.choice(faction_reactions)
    
    # Output the events
    print(f"\nRandom Tavern Event: {tavern_event}")
    print(f"Emmek Frewn's Action: {frewn_action}")
    print(f"Faction Involvement ({faction} - {pc_reputation.replace('_', ' ').capitalize()} Reputation): {faction_reaction}")

# Example: Generating random events and faction involvement
generate_random_event()
