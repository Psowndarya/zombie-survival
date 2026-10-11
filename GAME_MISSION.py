import random

# Player State tracking Health, Inventory, Score, and Completed Missions
player = {
    "health": 100,
    "inventory": [],
    "score": 0,
    "completed_missions": []
}

def show_status():
    """Displays current player stats including health, score, and inventory."""
    print("\n" + "="*50)
    print(f"❤️ Health: {player['health']} | 🏆 Score: {player['score']}")
    print(f"🎒 Inventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
    print("="*50)

def trigger_random_event():
    """Random events that occur after a mission to add bonus points or challenges."""
    events = [
        ("A sudden acid rain storm hits! You scramble for cover, losing a bit of health.", -10, 0),
        ("You find a hidden cache of old energy bars on the ground! Score bonus!", 0, 30),
        ("Nothing unusual happens. The wasteland remains eerily quiet.", 0, 0)
    ]
    
    event_message, health_change, score_change = random.choice(events)
    print(f"\n⚡ **Random Event:** {event_message}")
    
    if health_change != 0:
        player["health"] += health_change
        print(f"⚠️ Health changed by {health_change}")
    if score_change != 0:
        player["score"] += score_change
        print(f"🎉 Bonus! Score increased by {score_change}")

def mission_medicine():
    """Mission 1: Find Medicine"""
    print("\n🏥 **Mission 1: Find Medicine**")
    print("You receive a distress signal about an abandoned pharmacy across the ruined city.")
    print("1. Sneak through the sewers (Safer, but takes longer)")
    print("2. Run directly across the main highway (Risky, but fast)")
    
    choice = input("Choose your approach (1 or 2): ").strip()
    
    if choice == "1":
        print("\nYou silently navigate the damp sewers and successfully dodge hazards. You find the pharmacy untouched!")
        player["inventory"].append("Medicine")
        player["completed_missions"].append("Find Medicine")
        player["score"] += 50  # Adding points to score
        print("🎉 Success! [Medicine added] | 🏆 +50 Points")
    elif choice == "2":
        print("\nBandits spot you crossing the highway! You manage to escape with the medicine, but take damage.")
        player["health"] -= 20
        player["inventory"].append("Medicine")
        player["completed_missions"].append("Find Medicine")
        player["score"] += 25  # Adding fewer points for taking damage
        print("⚠️ Partial Success: Got medicine, lost 20 Health | 🏆 +25 Points")
    else:
        print("\n❌ Invalid choice! Hesitation cost you your window of opportunity. Mission Failed.")
        player["health"] -= 10

def mission_food():
    """Mission 2: Collect Food"""
    print("\n🥫 **Mission 2: Collect Food**")
    print("Your supplies are running low. You spot an old supermarket with potential rations.")
    print("1. Search the storage room in the back")
    print("2. Check the front cash registers and aisles")
    
    choice = input("Choose your search area (1 or 2): ").strip()
    
    if choice == "1":
        print("\nThe storage room is dark, but you uncover a stash of canned goods hidden under boxes.")
        player["inventory"].append("Canned Food")
        player["completed_missions"].append("Collect Food")
        player["score"] += 40  # Adding points to score
        print("🎉 Success! [Canned Food added] | 🏆 +40 Points")
    elif choice == "2":
        print("\nThe aisles are picked clean, and tripping over a shelf alerts scavengers. You flee empty-handed.")
        player["health"] -= 15
        print("❌ Mission Failed: No food found, and you lost 15 Health.")
    else:
        print("\n❌ Invalid choice! You spent too much time wandering around. Mission Failed.")

def mission_rescue():
    """Mission 3: Rescue a Survivor"""
    print("\n🤝 **Mission 3: Rescue a Survivor**")
    print("You hear someone tapping S.O.S. from inside a collapsed apartment building.")
    print("1. Clear the heavy debris carefully using tools")
    print("2. Force the jammed door open with brute strength")
    
    choice = input("Choose your rescue method (1 or 2): ").strip()
    
    if choice == "1":
        print("\nWorking methodically, you clear the rubble without causing a further collapse. The survivor is safe!")
        player["inventory"].append("Rescued Survivor")
        player["completed_missions"].append("Rescue Survivor")
        player["score"] += 70  # Adding points to score
        print("🎉 Success! [Survivor rescued] | 🏆 +70 Points")
    elif choice == "2":
        print("\nYour brute force causes the ceiling to shift! You pull the survivor out just in time, but get injured.")
        player["health"] -= 25
        player["inventory"].append("Rescued Survivor")
        player["completed_missions"].append("Rescue Survivor")
        player["score"] += 35  # Adding points to score
        print("⚠️ Partial Success: Survivor rescued, but you lost 25 Health | 🏆 +35 Points")
    else:
        print("\n❌ Invalid choice! The structure became too unstable while you hesitated. Mission Failed.")

def mission_selection_menu():
    """Main Mission Hub"""
    while True:
        show_status()
        print("\n📍 **Mission Selection Hub**")
        print("1. Find Medicine")
        print("2. Collect Food")
        print("3. Rescue a Survivor")
        print("4. Quit / End Game & View Final Score")
        
        choice = input("\nSelect a mission to undertake (1-4): ").strip()
        
        mission_completed = False
        
        if choice == "1":
            if "Find Medicine" in player["completed_missions"]:
                print("\n⚠️ You have already completed this mission! Choose another one.")
            else:
                mission_medicine()
                mission_completed = True
        elif choice == "2":
            if "Collect Food" in player["completed_missions"]:
                print("\n⚠️ You have already completed this mission! Choose another one.")
            else:
                mission_food()
                mission_completed = True
        elif choice == "3":
            if "Rescue Survivor" in player["completed_missions"]:
                print("\n⚠️ You have already completed this mission! Choose another one.")
            else:
                mission_rescue()
                mission_completed = True
        elif choice == "4":
            print(f"\n🏁 Game Ended. Final Score: {player['score']} points. Great work!")
            break
        else:
            print("\n❌ Invalid option. Please choose between 1 and 4.")
            
        # Trigger random event after a valid mission attempt
        if mission_completed and player["health"] > 0:
            trigger_random_event()
            
        # Check if player health is depleted
        if player["health"] <= 0:
            print(f"\n💀 Your health has reached 0! Game Over. Final Score: {player['score']}")
            break

if __name__ == "__main__":
    print("🎮 Welcome to the Post-Apocalyptic Survival Game")
    mission_selection_menu()