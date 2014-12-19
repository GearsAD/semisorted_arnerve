'''
Created on Dec 12, 2014

@author: gearsad
'''
import apriltags_clibrary
import cv2
import numpy as np
import lcm
from user_update_t import user_update_t
from kinect_update_t import kinect_update_t
from kinect_rawdata_t import kinect_rawdata_t
from numpy import uint8

detector = None
currentImage = None
videoWriter = None

def ProcessImageForAprilTags(openCVMatImg):
    '''
    Process an OpenCV image (greyscale) for AprilTags
    '''
    # Copy the buffer into C-Space using the SWIG interop.
    flat = openCVMatImg.flatten()
    tempBuffer = np.asarray(flat).tostring()
    tgtBuffer = apriltags_clibrary.ARNerve_Imageu8_GetBuffer(currentImage)
    stride = apriltags_clibrary.ARNerve_Imageu8_GetStride(currentImage)
    if openCVMatImg.shape[1] % stride == 0: #Can copy directly:
        apriltags_clibrary.memmove(tgtBuffer, tempBuffer) 
    else:
        raise Exception("The original image does not have width=stride, and that case has not been implemented yet. The Kinect is giving me 1920x1080, which won't have this issue so not a lot of effort is spent for these generic cases - sorry! [GearsAD]")
    # Have a look-see at what it thinks it has
    #apriltags_clibrary.image_u8_write_pnm(currentImage, 'output_intermediate.pnm')
    
    # Get the detections.
    detections = apriltags_clibrary.apriltag_detector_detect(detector, currentImage)
    
    # Process them.
    cnt = apriltags_clibrary.zarray_size(detections)
    if cnt > 0:
        print "Number of fiducials detected = {0}".format(cnt)
        for index in xrange(0, cnt):
            # Using the helper function defined in the SWIG interface file
            detection = apriltags_clibrary.ARNerve_GetDetection(index, detections)
            
            print "Detection {0}, X = {1}, Y = {2}".format(index, \
                                                           apriltags_clibrary.ARNerve_GetDetection_Coord_X(detection), \
                                                           apriltags_clibrary.ARNerve_GetDetection_Coord_Y(detection))
        pass
    
    return detections

def DrawDetectionsOnImage(image, detections):
    '''
    Draw the AprilTag detections on the OpenCV image with red boxes.
    '''
    cnt = apriltags_clibrary.zarray_size(detections)
    if cnt > 0:
#        print "Number of features detected = {0}".format(cnt)
        for index in xrange(0, cnt):
            # Using the helper function defined in the SWIG interface file
            detection = apriltags_clibrary.ARNerve_GetDetection(index, detections)
            x = int(apriltags_clibrary.ARNerve_GetDetection_Coord_X(detection))
            y = int(apriltags_clibrary.ARNerve_GetDetection_Coord_Y(detection))
            
            #Ref: http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-functions
            cv2.rectangle(image, (x-20, y-20), (x+20, y+20), (0, 0, 255), 8)
            #cv2.putText(image, str(index), (x+20,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
        pass
    
        
    cv2.putText(image, "AprilTag Fiducials = " + str(cnt), (20,40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
    return image

def lcmKinect_handler(channel, data):
    userUpdate = user_update_t.decode(data)
    kinectRawData = userUpdate.kinect.camera_update
    if len(kinectRawData.rgb_jpg) > 0:
        # Do a frame update
        #REF OpenCV: docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html
        data = np.asarray(bytearray(kinectRawData.rgb_jpg), dtype=np.uint8)
        img = cv2.imdecode(data, 0) #Greyscale for now...
        if img is not None:
            #cv2.imwrite("TestOutput.jpg", img)
            #Flip it first, as it's left<->right mirrored
            #Ref: http://docs.opencv.org/modules/core/doc/operations_on_arrays.html#void%20flip%28InputArray%20src,%20OutputArray%20dst,%20int%20flipCode%29
            temp = img
            imgFlipped = np.fliplr(img)
            # If it's not contiguous, make it so
            if not imgFlipped.flags.contiguous:
                imgFlipped = imgFlipped.copy()
            detections = ProcessImageForAprilTags(imgFlipped)

            # Process the image.
            backtorgb = cv2.cvtColor(imgFlipped,cv2.COLOR_GRAY2RGB)
            dacktorgb = DrawDetectionsOnImage(backtorgb, detections)

            # Show it
            smallimg = cv2.resize(backtorgb, (1920/2, 1080/2))
            cv2.cv.ShowImage("OpenCV",cv2.cv.fromarray(smallimg))
            videoWriter.write(smallimg)
    #print("Got update!")
    
if __name__ == '__main__':
    # Create the LCM channel
    lc = lcm.LCM()
    subscription = lc.subscribe("ARNerve_UserUpdates", lcmKinect_handler)
    
    # Load the AprilTag SWIG module
    # REF: http://www.swig.org/Doc2.0/SWIGDocumentation.html#Preface_nn2
    detector = apriltags_clibrary.apriltag_detector_create()
    apriltags_clibrary.apriltag_detector_add_family(detector, apriltags_clibrary.tag36h11_create())
    
    # Create the AprilTags image.
    
    currentImage = apriltags_clibrary.image_u8_create(1920, 1080)
    
    #Ref http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html
    videoWriter = cv2.VideoWriter("outputBot.avi", cv2.cv.FOURCC('X', 'V', 'I', 'D'), 20, (1920/2, 1080/2) )
    #newImg = cv2.imread('/home/gearsad/semisorted_arnerve/arnerve_bot/apriltags_interpreter/Debug/test_goodstride.pnm', 0)
    #ProcessImageForAprilTags(newImg)
    #Ref: http://stackoverflow.com/questions/8163976/how-python-can-get-binary-datachar-from-c-by-swig
    #testBuffer = np.ones(1920*1080, dtype=uint8) * 128
    
    
    # Create an openCV window
    cv2.cv.NamedWindow("OpenCV", cv2.WINDOW_NORMAL)
    cv2.cv.StartWindowThread()
    cv2.cv.ResizeWindow("OpenCV", 640, 480)
    try:
        while True:
            i = 0
            lc.handle()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    
    pass