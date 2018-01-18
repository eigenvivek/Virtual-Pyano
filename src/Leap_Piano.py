import os, sys, inspect, time, thread
sys.path.insert(0, "../lib")
import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

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
        
        # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
        #       frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
              
              
        app_width = 600
        # app_length = 200
        i_box = frame.interaction_box




        for hand in frame.hands:

            hand_pointables = hand.pointables
            # print type(hand_pointables)

            # tip = hand_pointables[1].tip_position # GIVES POSITION OF TIP OF INDEX FINGER!!!!!
            # print tip
            
            normalized_tip = i_box.normalize_point(hand_pointables[1].tip_position)
            app_x = app_width  * normalized_tip.x
            # app_z = app_length * (1 - normalized_tip.z)
            
            # print "X: %d, Z: %d" % (app_x, app_z)
            
            app_x = round(app_x)
            
            if app_x in range(0,99):
                print "C"
            elif app_x in range(100,199):
                print "D"
            elif app_x in range(200,299):
                print "E"
            elif app_x in range(300,399):
                print "G"
            elif app_x in range(400,499):
                print "A"
            elif app_x in range(500,599):
                print "C"
            
            
                
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