import sys

# Import the LEAP library
sys.path.insert(0, "../lib")
import Leap

# Import the Piano class
import construct_piano
piano = construct_piano.Piano(sys.argv[1], sys.argv[2])
keys = construct_piano.Keys(piano)

# Create the Listener Class
class Listener(Leap.Listener):

    # Initializing functions
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"


    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # Create a box for scaling all positions by
        i_box = frame.interaction_box


        for hand in frame.hands:

            # Get all the information about the fingers in frame
            hand_pointables = hand.pointables

            # Find and normalize all tip locations
            normalized_hand_positions = []
            for i in range(len(hand_pointables)):
                tip = hand_pointables[i].tip_position
                normalized_tip = i_box.normalize_point(tip)
                normalized_hand_positions.append(normalized_tip)

            # Pass the pointables in the Keys class
            keys.master(normalized_hand_positions)
            if len(keys.pressed) != 0:
                print keys.pressed


def main():
    # Print the scale
    print "The scale is: " + str(keys.scale)

    # Create a sample listener and controller
    listener = Listener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
