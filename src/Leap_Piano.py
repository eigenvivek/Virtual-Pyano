import sys
sys.path.insert(0, "../lib")
import Leap


class SampleListener(Leap.Listener):
        
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    
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
        
              
              
        app_width = 4
        app_height = 200
        
        
        i_box = frame.interaction_box




        for hand in frame.hands:

            hand_pointables = hand.pointables
            # print type(hand_pointables)

            # tip = hand_pointables[1].tip_position # GIVES POSITION OF TIP OF INDEX FINGER!!!!!
            # print tip
            
            normalized_tip = i_box.normalize_point(hand_pointables[1].tip_position)
            app_x = app_width  * normalized_tip.x
            app_y = app_height * normalized_tip.y
            
            print "X: %d, Y: %d" % (app_x, app_y)
                        
            notes = ['C', 'D', 'E', 'F', 'G']
            
            if app_y < 30:
                print notes[int(app_x)]
            else:
                print "No note pressed"
            # elif app_x in range(500,599):
            #     print "C"
            
            
                
def main():
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