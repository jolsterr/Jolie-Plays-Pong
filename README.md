# Pong: A family-fun Pong game for all

## Going back to the Classics with Turtle
#### Using the Turtle module for graphics, I created a simple game of pong for two competing players using the same console (in this case a keyboard). Player A presses W or S to move and Player B presses the Up or Down keys to move. In this script, the key functions used were:
- A Main Game Loop (consisting of moving the ball, checking the borders, and collisions) 
- Keyboard Binding (wn.onkey())
- Moving the cordinates of the pieces.
## With Sound
The Repository contains a pong game without sound and with sound as respectively named. Sound is only available for devices on MacOS (for Linux, replace `os.system(afplay bump2.wav&)` with `os.system(aplay bump2.wav&)` and for Windows `import winsound`, then replace `os.system(afplay bump2.wav&)` with `winsound.PlaySound("bump2.wav", winsound.SND_ASYNC)`.
## Audio File 
Attached as bump2.wav
