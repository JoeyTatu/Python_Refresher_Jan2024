class StoryNode:
    def __init__(self, text, choices=None):
        self.text = text
        self.choices = choices or {}

    def add_choice(self, choice, destination):
        self.choices[choice] = destination

    def get_choice(self):
        print(self.text)
        for i, choice in enumerate(self.choices.keys(), 1):
            print(f"{i}. {choice}")
        
        while True:
            try:
                choice_index = int(input("Choose an option: "))
                return list(self.choices.values())[choice_index - 1]
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid option.")

start_node = StoryNode("You find yourself in a dark room. What do you do?")
next_node1 = StoryNode("You decide to explore the room. You find a key.", {"Take the key": "unlock_door", "Ignore it": "ignore_key"})
next_node2 = StoryNode("You ignore the key and continue to explore. You find a mysterious door.", {"Open the door": "treasure_room", "Leave the door alone": "leave_door"})
unlock_door_node = StoryNode("You use the key to unlock the door. It leads to a corridor.", {"Continue down the corridor": "treasure_room", "Go back to the dark room": "start"})
treasure_room_node = StoryNode("You enter a room filled with treasures. Congratulations, you win!", {})

nodes = {
    "start": start_node,
    "next_node1": next_node1,
    "next_node2": next_node2,
    "unlock_door": unlock_door_node,
    "treasure_room": treasure_room_node,
}

start_node.add_choice("Explore the room", "next_node1")
start_node.add_choice("Leave the room", "treasure_room")

current_node = nodes["start"]
while current_node.choices:
    next_node_name = current_node.get_choice()
    current_node = nodes[next_node_name]

print("Game over.")