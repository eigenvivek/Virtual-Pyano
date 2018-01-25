import sys

# Import the LEAP library
sys.path.insert(0, "../lib")
import Leap

"""
Declare some global values:
    - Step values
    - Notes
    - Scale formulas
"""
# Step values
R = 0 # Root
H = 1 # Half step
W = 2 # Whole step
B = 3 # 'Big' 1.5 step

# Provide all notes
note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Intervals for different modes
scale_formulas = {
    'major': [R, W, W, H, W, W, W, H],
    'natural_minor': [R, W, H, W, W, H, W, W],
    'harmonic_minor': [R , W, H, W, W, H, B, H],
    'dorian': [R, W, H, W, W, W, H, W],
    'mixolydian': [R, W, W, H, W, W, H, W],
    'ahava_raba': [R, H, B, H, W, H, W, W],
    'blues': [R, B, W, H, H, B, W],
    'major_pentatonic': [R, W, W, B, W]
}

"""The main class for a piano:"""
class Piano:

    # Initialize the piano
    def __init__(self, root, mode):

        self.root = root
        self.mode = mode

    # Return the scale the piano will use
    def make_scale(self):

        # Find the starting index of the scale
        start = note.index(self.root)

        # Reorder the set of notes such that the root is index 0
        reordered = note[start:] + note[:start]

        # Return the scale formula based on the mode requested by the user
        formula = scale_formulas[self.mode]

        # Construct the new scale
        scale = []
        index = 0

        for i in range(len(formula)-1):
            index += formula[i]
            scale.append(reordered[index])

        scale += scale[0]
        return scale



"""Create a class to track if keys are pressed"""
class Keys:

    # Initialize the keys and the interaction_box
    def __init__(self, Piano):

        self.scale = Piano.make_scale()
        self.appbox = self.make_ibox()

    def make_ibox(self, app_height = 200, app_length = 100):

        # The number of keys this piano will have
        num_keys = len(self.scale)

        # Give the length of the piano
        app_width = num_keys - 1

        appbox = [app_width, app_height, app_length]
        return appbox


    def scale_normalized_position(self, normalized_tip):

        # Declare an empty array
        position_vector = []

        # Scale the position
        app_x = self.appbox[0] * normalized_tip.x
        app_y = self.appbox[1] * normalized_tip.y
        app_z = self.appbox[2] * normalized_tip.z

        # Add the scaled values to the array
        for coord in [app_x, app_y, app_z]:
            coord = round(coord)
            position_vector.append(coord)

        # Return the position vector
        return position_vector


    def test_xcoords(self, position_vector, x_coords):


        # Test relevancy
        if position_vector[1] < 10:
            if position_vector[2] in range(35,50):
                x_coords.append(position_vector[0])


    def find_pressed(self, x_coords):
        pressed = []

        if len(x_coords) == 0:
            print "No notes pressed!"

        else:

            for i in range(len(x_coords)):

                current_note = self.scale[int(x_coords[i])]
                pressed.append(current_note)

        return pressed


    def master(self, normalized_hand_positions):
        """
        `master` takes `pointables` object from the main function and determines
        which keys are being pressed during the current frame'
        """

        # Declare array to store relevant x_coords
        x_coords = []

        # hand_pointables is a list with the positions of all finger tips in frame
        for i in range(len(normalized_hand_positions)):

            # Get individual tips
            normalized_tip = normalized_hand_positions[i]

            # Scale the (x,y,z) coordinates of the tip's position
            position_vector = self.scale_normalized_position(normalized_tip)

            # Test position to see if it is relevant
            self.test_xcoords(position_vector, x_coords)

        # Find the notes being pressed
        self.pressed = self.find_pressed(x_coords)
