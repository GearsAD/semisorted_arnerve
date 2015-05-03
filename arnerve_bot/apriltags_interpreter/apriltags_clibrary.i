%module apriltags_clibrary
%{
/* Put headers and other declarations here */
#include "common/zarray.h"
#include "common/image_u8.h"
#include "apriltag.h"
#include "tag36h11.h"
%}

/*Include the important files*/
%include "common/zarray.h"
%include "common/image_u8.h"
%include "apriltag.h"
%include "tag36h11.h"
//Ref: http://stackoverflow.com/questions/8163976/how-python-can-get-binary-datachar-from-c-by-swig
%include "cdata.i"

// Helper functions to get the detections
%inline %{
apriltag_detection_t* ARNerve_GetDetection(int index, zarray_t *detections)
{
	apriltag_detection_t *det;
  	zarray_get(detections, index, &det);
	return det;
}
float ARNerve_GetDetection_Coord_X(apriltag_detection_t *detection)
{
	return detection->c[0];
}
float ARNerve_GetDetection_Coord_Y(apriltag_detection_t *detection)
{
	return detection->c[1];
}
int ARNerve_Imageu8_GetWidth(image_u8_t *image)
{
	return image->width;
}
int ARNerve_Imageu8_GetHeight(image_u8_t *image)
{
	return image->height;
}
int ARNerve_Imageu8_GetStride(image_u8_t *image)
{
	return image->stride;
}
void* ARNerve_Imageu8_GetBuffer(image_u8_t *image)
{
	//Modified from the copy method in image_u8.
    return image->buf;
}
void ARNerve_Imageu8_CopyToBuffer(image_u8_t *image, void *newbufferdata, int bytelength)
{
	//Modified from the copy method in image_u8.
    memcpy(image->buf, newbufferdata, bytelength);
}
%}