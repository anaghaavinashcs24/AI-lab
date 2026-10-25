class FourRoomVacuumAgent:
    def __init__(self, initial_location='A', room_status=None):
        # Create 4 rooms A, B, C, D with clean/dirty status[cite: 1]
        self.location = initial_location
        self.rooms = room_status if room_status else {
            'A': 'dirty', 
            'B': 'dirty', 
            'C': 'dirty', 
            'D': 'dirty'
        }

    def run(self):
        print(f"Initial State -> Vacuum Position: {self.location}, Rooms: {self.rooms}") #[cite: 1, 2]
        
        # while any room is dirty[cite: 1]
        while any(status == 'dirty' for status in self.rooms.values()):
            current_room = self.location
            
            # if current room is dirty then suck dirt and mark clean[cite: 1]
            if self.rooms[current_room] == 'dirty':
                print(f"Room {current_room} is dirty. Action: suck dirt.") #[cite: 1, 2]
                self.rooms[current_room] = 'clean' #[cite: 1]
                print(f"Marked Room {current_room} as clean.") #[cite: 1]
            # Movement transitions[cite: 1, 2]
            elif current_room == 'A':
                self.location = 'B'
                print("Move right -> B") #[cite: 1]
            elif current_room == 'B':
                self.location = 'D'
                print("Move down -> D") #[cite: 2]
            elif current_room == 'D':
                self.location = 'C'
                print("Move left -> C") #[cite: 2]
            elif current_room == 'C':
                self.location = 'A'
                print("Move up -> A") #[cite: 2]
                
        print("Stop. All rooms are clean.") #[cite: 1, 2]

# Example Usage:
agent_4room = FourRoomVacuumAgent(initial_location='A', room_status={'A': 'dirty', 'B': 'dirty', 'C': 'dirty', 'D': 'dirty'})
agent_4room.run()