class TwoRoomVacuumAgent:
    def __init__(self, initial_location='A', room_status=None):
        # Initialise location of vacuum cleaner and status of Room A and Room B
        self.location = initial_location
        self.rooms = room_status if room_status else {'A': 'dirty', 'B': 'dirty'}

    def run(self):
        print(f"Initial State -> Location: {self.location}, Rooms: {self.rooms}")
        
        # while Room A or Room B is dirty do[cite: 1]
        while self.rooms['A'] == 'dirty' or self.rooms['B'] == 'dirty':
            current_room = self.location
            
            # if current room is dirty then[cite: 1]
            if self.rooms[current_room] == 'dirty':
                print(f"Room {current_room} is dirty. Suck the dirt.") #[cite: 1]
                self.rooms[current_room] = 'clean' #[cite: 1]
                print(f"Marked Room {current_room} cleaned.") #[cite: 1]
            else:
                # else if current location is A -> move to room B, else -> move to room A[cite: 1]
                if self.location == 'A':
                    self.location = 'B'
                    print("Move to room B.") #[cite: 1]
                else:
                    self.location = 'A'
                    print("Move to room A.") #[cite: 1]
                    
        print("Stop. All rooms are clean.") #[cite: 1]

# Example Usage:
agent = TwoRoomVacuumAgent(initial_location='A', room_status={'A': 'dirty', 'B': 'dirty'})
agent.run()