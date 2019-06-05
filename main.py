# We use ZMQ to talk to the game server. The basic
# communication is set up so you shouldn't need to worry about it much
import zmq
import sys
import random

PORT = 5556

# Connect to the game server,
# Make sure it is running
print("Connecting to server")

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f'tcp://127.0.0.1:{PORT}')

print("Connected to server")

# Connect to the server using it's API
socket.send_string('start')

# Create a board to reference for available moves
# String from message server prints in format:
# '.' for blank space
# ',' for space delimiter
# ';' for line delimiter
# Numbers are based off counting from original string, skipping 1 number to account for delimiters
board = {0: "0,0",
         2: "0,1",
         4: "0,2",
         6: "1,0",
         8: "1,1",
         10: "1,2",
         12: "2,0",
         14: "2,1",
         16: "2,2"}

# Make this function, using whatever other classes / functions you need
def get_move():
    
    check_board()

    # Try to block computer moves if it is about to win (only 8 ways to win)
    next = current
    next = next.replace(";","")
    next = next.replace(",","")

    # 3 horizontal lines
    line1 = next[0:3]
    line2 = next[3:6]
    line3 = next[6:]

    # 3 vertical lines
    line4 = next[0] + next[3] + next[6]
    line5 = next[1] + next[4] + next[7]
    line6 = next[2] + next[5] + next[8]

    # 2 diagonal lines
    line7 = next[0] + next[4] + next[8]
    line8 = next[2] + next[4] + next[6]

    if line1.count(pcId) >= 2 and line1.count(".") == 1:
        return "0," + str(line1.find("."))
    if line2.count(pcId) >= 2 and line1.count(".") == 1:
        return "1," + str(line1.find("."))
    if line3.count(pcId) >= 2 and line1.count(".") == 1:
        return "2," + str(line1.find("."))

    if line4.count(pcId) >= 2 and line4.count(".") == 1:
        return str(line4.find(".")) + ",0"
    if line5.count(pcId) >= 2 and line5.count(".") == 1:
        return str(line5.find(".")) + ",1"
    if line6.count(pcId) >= 2 and line6.count(".") == 1:
        return str(line6.find(".")) + ",2"

    line7Moves = {0: "0,0",
                  1: "1,1",
                  2: "2,2"}
    
    line8Moves = {0: "0,2",
                  1: "1,1",
                  2: "2,0"}

    if line7.count(pcId) >= 2 and line7.count(".") == 1:
        return line7Moves[line7.find(".")]
    if line8.count(pcId) >= 2 and line8.count(".") == 1:
        return line8Moves[line8.find(".")]

    # Generate a random number to select one of the moves left if not blocking pc's move
    movesLeft = len(board)
    if movesLeft > 0:
        return list(board.values())[random.randint(0,movesLeft-1)]
    

# Function to check open spots and remove occupied spots
def check_board():
    for i,k in enumerate(current):
        if k == id or k == pcId:
            try:
                board.pop(i)
            except KeyError:
                continue


while True:
    sys.stdout.flush()

    # Get the next message from the server. Note that it may be multi-line
    message = socket.recv_string()

    # If the server reply has 'done' in it, the game is finished
    if 'done' in message:
        break
    
    # Split the message and extract relevant info
    for line in message.split("\n"):
        if "settings" in line:
            if "your_id" in line:
                id = line[-1]
                if id == "x":
                    pcId = "o"
                elif id == "o":
                    pcId = "x"
            if "board_size" in line:
                boardSize = line[-3:]
        if "update board" in line:
            current = line[-17:]

    # View current board
    print(current)

    # Message contains game state information,
    # You'll want to parse message and construct
    # a valid response
    reply = get_move()

    # Send reply to the server
    socket.send_string(reply)
