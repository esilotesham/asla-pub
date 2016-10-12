
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, './lib'))
sys.path.insert(0, lib_dir)
import Leap


def main():
    get_leap_input()



def get_leap_input():
    # Create a controller object
    controller = Leap.Controller()
    # Wait till controller is connected
    while not controller.is_connected:
        pass
    print controller.is_service_connected()

    while controller.is_connected:
        # Uncomment if you want to enable gestures
        # controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        # controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        # controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        # controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

        # Get a frame object
        frame = controller.frame()
        hands = frame.hands
        # for gesture in frame.gestures():
        #     if gesture.type == Leap.Gesture.TYPE_CIRCLE:
        #         print "circle"
        #     elif gesture.type == Leap.Gesture.TYPE_SWIPE:
        #         print "Swipe"
        #     elif gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
        #         print "screen tap"
        #     elif gesture.type == Leap.Gesture.TYPE_KEY_TAP:
        #         print "key tap"
        for hand in hands:
            if hand.is_right:
                print hand.confidence
                # if hand.confidence >= 0.95:
                #     for finger in frame.fingers:
                #         if finger.is_extended:
                #             print finger.type
                #     break
                    # FingersNr, 1.000000
                    # FingertipsDistances, 119.432000, 0.000000, 0.000000, 0.000000, 0.000000
                    # FingertipsDistancesRefined, 118.178000, 0.000000, 0.000000, 0.000000, 0.000000
                    # FingertipsInterDistances, 0.000000, 0.000000, 0.000000, 0.000000
                    # FingertipsPositions, -46.136100, 0.000000, 0.000000, 0.000000, 0.000000, 373.222000, 0.000000, 0.000000, 0.000000, 0.000000, 167.696000, 0.000000, 0.000000, 0.000000, 0.000000
                    # HandDirection, -0.093860, 0.623742, -0.775974
                    # HandSphereCenter, -37.439500, 310.239000, 207.670000
                    # HandSphereRadius, 66.902700
                    # PalmNormal, 0.135235, -0.764203, -0.630638
                    # PalmPosition, -24.617900, 262.241000, 206.220000
                    # PalmPositionRefined, -34.073800, 258.231000, 192.139000
                    # PalmVelocity, 24.019400, 46.745400, -12.472800
                    # RotationAngle, 0.003719
                    # RotationAxis, 0.500481, -0.569983, 0.651643
                    # RotationMatrix, 0.999995, 0.002406, 0.002108, -0.002410, 0.999995, 0.001847, -0.002104, -0.001852, 0.999996
                    # RotationProbability, 0.000091
                    # ScaleFactor, 1.000000
                    # ScaleProbability, 0.000007
                    # Translation, 33.952900, 20.824800, 67.488200
                    # TranslationProbability, 0.999902

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
