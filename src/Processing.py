import sound
import config
import math

# initialize necessary sounds/scale
scale = ('C', 'D', 'E', 'F', 'G', 'A', 'B', 'C')
snd = sound.Sound()

V_THRESH = config.V_THRESH
NOTE_WIDTH = config.NOTE_WIDTH
X_MIN = config.X_MIN
X_MAX = config.X_MAX
PIANO_CENTER=len(snd.notesByIndex)/2 
padding = NOTE_WIDTH/10

note_cutoffs = range(X_MIN,X_MAX+NOTE_WIDTH, NOTE_WIDTH)
piano_size = len(note_cutoffs)
snd.setCurrentPiano(PIANO_CENTER-piano_size/2, PIANO_CENTER+piano_size/2)


def position_to_note_played(pos):

	for hand in pos.right, pos.left:
		for finger in hand:
			if finger.y < V_THRESH:
				if finger.x > X_MIN and finger.x < X_MAX:
					for i in range(1,len(note_cutoffs)):
						if finger.x > note_cutoffs[i-1]+padding and finger.x < note_cutoffs[i]-padding:
							startPlaying(finger, i-1)
				else:
					stopPlaying(finger)
			else:
				stopPlaying(finger)


def startPlaying(finger, note):
	if finger.notePlaying != None and note != finger.notePlaying:
		snd.noteOffByIndex(finger.notePlaying)
	finger.notePlaying = note
	snd.playNoteByIndex(finger.notePlaying)

def stopPlaying(finger):
	if finger.notePlaying != None:
		snd.noteOffByIndex(finger.notePlaying)
	finger.notePlaying = None



