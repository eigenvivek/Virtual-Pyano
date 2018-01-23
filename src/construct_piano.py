import sys

"""Declare some global values:"""
# Step values
R = 0 # Root
H = 1 # Half step
W = 2 # Whole step
B = 3 # 'Big' 1.5 step

# Provide all notes
note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

interval_relations = {
    'major': [R, W, W, H, W, W, W, H],
    'natural_minor': [R, W, H, W, W, H, W, W],
    'harmonic_minor': [R, W, H, W, W, H, B, H],
    'dorian': [R, W, H, W, W, W, H, W],
    'mixolydian': [R, W, W, H, W, W, H, W],
    'ahava_raba': [R, H, B, H, W, H, W, W],
    'blues': [R, B, W, H, H, B, W]
}

"""The main class for a piano:"""   
class Piano:
    
    def __init__(self, root, mode):
        
        self.root = root
        self.mode = mode
        self.scale = self.make_scale()
        
    def make_scale(self):
        
        # Find the starting index of the scale
        start = note.index(self.root)
        
        # Reorder the set of notes such that the root is index 0
        reordered = note[start:] + note[:start]
        
        # Return the scale formula based on the mode requested by the user
        formula = interval_relations[self.mode]
        
        # Construct the new scale
        scale = []
        index = 0
        
        for i in range(len(formula)-1):
            index += formula[i]
            scale.append(reordered[index])
            
        scale += scale[0]
        return scale
    