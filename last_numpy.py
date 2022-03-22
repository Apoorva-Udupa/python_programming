'''python datacamp numpy -->
Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
Extract all the heights of all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
Do the same for the other players. Print out their median height. Replace None with the correct code.'''
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions=='GK']
#print(gk_heights)

# Heights of the other players: other_heights
other_heights = np_heights[np_positions!='GK']

# Print out the median height of goalkeepers. Replace 'None'
med = np.median(gk_heights)
print("Median height of goalkeepers: " + str(med))

# Print out the median height of other players. Replace 'None'
med2 = np.median(other_heights)
print("Median height of other players: " + str(med2))
