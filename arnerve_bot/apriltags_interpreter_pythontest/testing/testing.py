'''
Created on Dec 9, 2014

@author: gearsad
'''
import sys
#sys.path.append("/home/gearsad/semisorted_arnerve/arnerve_bot/apriltags_interpreter/Debug")
import apriltags_clibrary
from cv2.cv import *
from numpy import reshape


if __name__ == '__main__':

    img = LoadImage("/home/gearsad/semisorted_arnerve/media/Kinect References/wall_reference.pnm", 0)
    NamedWindow("opencv")
    ShowImage("opencv",img)
    WaitKey(0)
    
    # Ref: http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html
    # Best Ref ever: http://docs.opencv.org/index.html
    dims = GetDims(img)
    print dims
    print img[0, 0]
    #retval, data = imencode()
    
    
    # Load the module
    # REF: http://www.swig.org/Doc2.0/SWIGDocumentation.html#Preface_nn2
    det = apriltags_clibrary.apriltag_detector_create()
    apriltags_clibrary.apriltag_detector_add_family(det, apriltags_clibrary.tag36h11_create())
    
    image = apriltags_clibrary.image_u8_create_from_pnm('/home/gearsad/semisorted_arnerve/media/Kinect References/wall_reference2.pnm')
    print image
    
    detections = apriltags_clibrary.apriltag_detector_detect(det, image)
    
    cnt = apriltags_clibrary.zarray_size(detections)
    print "Number of features detected = {0}".format(cnt)
    for index in xrange(0, cnt):
        # Using the helper function defined in the SWIG interface file
        detection = apriltags_clibrary.ARNerve_GetDetection(index, detections)
        
        print "Detection {0}, X = {1}, Y = {2}".format(index, \
                                                       apriltags_clibrary.ARNerve_GetDetection_Coord_X(detection),
                                                       apriltags_clibrary.ARNerve_GetDetection_Coord_Y(detection))
    pass