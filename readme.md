# Senseye's Coding Task

This is a small coding project to showcase your ability in coding. The idea
is that it is a simple task, with plenty of room to show off your ability.

## The Task
The task is to create a tic-tac-toe bot that communicates with a game server.
It's okay if the bot isn't a perfect player, we are more curious is how well
you can understand a problem, and start to design and construct a solution. If
the bot chose random moves, but all the code around it was clean and well thought out,
that is fine. However, feel free to embellish and show off your coding skills.
Try to shoot for how much you can do in around 2 hours.

## Setup
To start you'll need Python 3.6.
The only package requirement is zmq: `pip install pyzmq`.

To run the server, there are three options:
    1. Run the pyc file `python3 ./bin/server.pyc`
    2. Run the Mac binary: `./bin/server`
    2. Run the Windows binary: `./bin/server.exe`
Once this is up, you can run your code `python3 main.py` to communicate with the server.
The server should give output about what is happening.

### Note:
Some feedback was given that the server does not give enough verbose output. 
If the game ends for any reason, it will not show the final board state.
Apologies for this, will fix "soon"

## Communcation API
The server and client communicate through ZMQ. The server has been compiled
to obfuscate the code, since the server and client should end up being very similar.

The server will send strings to update the games state. It can send multiple commands at
once seperated by newline characters (`\n`)

### Messages from the server
- `settings your_id {X}`: Tells you whether your mark is 'x' or 'o'. 'x' Goes first.
- `settings board_size {w},{h}`: Width and Height of the board. For this server it is always 3x3
- `update board [...]`: Board state denoted by the following:
    - `.`: empty space
    - `x`: X Player
    - `o`: O player
    - `,`: cell seperator
    - `;`: row seperator
- `action`: Command to request an action from your bot.
- `done <message>`: Command denote that the game is complete, with a message of why it ended

### Messages to the server
- `start`: Tell the server to start a game
- `{row},{col}`: Position of your move, in response to an `action`. If an invalid move is entered,
or the server cannot parse your move, the game ends

### Example:
client: `start`

server:
```
settings your_id o
settings board_size 3,3
update board .,.,.;.,.,.;.,o,.
action
```

client: `0,1`

server:
```
update board .,o,.;.,.,x;.,x,.
action
```

## Submission
To submit, reply to the workable hiring email that this task was sent to you with (Jessica or Alex). 
If you remove the bin folder, it should be small enough to attach as an email

Don't hesitate to ask any questions or clarifications!

## Known Bugs
There are some bugs with the server that some candidates have pointed out with the server. 


