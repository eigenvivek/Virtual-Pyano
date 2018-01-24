import sys

# Import the LEAP library
sys.path.insert(0, "../lib")
import Leap

# Import the Piano class
import construct_piano

piano = construct_piano.Piano(sys.argv[1], sys.argv[2])

class SampleListener(Leap.Listener):
    
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
        
        app_width = len(piano.scale) - 1
        app_height = 200
        
        i_box = frame.interaction_box


        for hand in frame.hands:

            hand_pointables = hand.pointables
            # print type(hand_pointables)

            # tip = hand_pointables[1].tip_position # GIVES POSITION OF TIP OF INDEX FINGER!!!!!
            # print tip
            
            normalized_tip = i_box.normalize_point(hand_pointables[1].tip_position)
            
            x_coords = []
            for i in range(len(hand_pointables)):
                
                normalized_tip = i_box.normalize_point(hand_pointables[i].tip_position)
                
                app_y = app_height * normalized_tip.y
                if app_y < 10:
                    app_x = app_width  * normalized_tip.x
                    x_coords.append(app_x)
            
            
            
            # print "X: %d, Y: %d" % (app_x, app_y)

            if len(x_coords) > 0:
                pressed = []
                for i in range(len(x_coords)):
                    
                    pressed.append(piano.scale[int(x_coords[i])])
                    
                print pressed
            else:
                print "No notes pressed!"
            
           
def main():
    # Print the scale
    print "The scale is: " + str(piano.scale)
    
    # Create a sample listener and controller
    listener = SampleListener()
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