# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_apriltags_clibrary', [dirname(__file__)])
        except ImportError:
            import _apriltags_clibrary
            return _apriltags_clibrary
        if fp is not None:
            try:
                _mod = imp.load_module('_apriltags_clibrary', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _apriltags_clibrary = swig_import_helper()
    del swig_import_helper
else:
    import _apriltags_clibrary
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class zarray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zarray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zarray, name)
    __repr__ = _swig_repr
    __swig_setmethods__["el_sz"] = _apriltags_clibrary.zarray_el_sz_set
    __swig_getmethods__["el_sz"] = _apriltags_clibrary.zarray_el_sz_get
    if _newclass:el_sz = _swig_property(_apriltags_clibrary.zarray_el_sz_get, _apriltags_clibrary.zarray_el_sz_set)
    __swig_setmethods__["size"] = _apriltags_clibrary.zarray_size_set
    __swig_getmethods__["size"] = _apriltags_clibrary.zarray_size_get
    if _newclass:size = _swig_property(_apriltags_clibrary.zarray_size_get, _apriltags_clibrary.zarray_size_set)
    __swig_setmethods__["alloc"] = _apriltags_clibrary.zarray_alloc_set
    __swig_getmethods__["alloc"] = _apriltags_clibrary.zarray_alloc_get
    if _newclass:alloc = _swig_property(_apriltags_clibrary.zarray_alloc_get, _apriltags_clibrary.zarray_alloc_set)
    __swig_setmethods__["data"] = _apriltags_clibrary.zarray_data_set
    __swig_getmethods__["data"] = _apriltags_clibrary.zarray_data_get
    if _newclass:data = _swig_property(_apriltags_clibrary.zarray_data_get, _apriltags_clibrary.zarray_data_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_zarray()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_zarray
    __del__ = lambda self : None;
zarray_swigregister = _apriltags_clibrary.zarray_swigregister
zarray_swigregister(zarray)


def zarray_create(*args):
  return _apriltags_clibrary.zarray_create(*args)
zarray_create = _apriltags_clibrary.zarray_create

def zarray_destroy(*args):
  return _apriltags_clibrary.zarray_destroy(*args)
zarray_destroy = _apriltags_clibrary.zarray_destroy

def zarray_copy(*args):
  return _apriltags_clibrary.zarray_copy(*args)
zarray_copy = _apriltags_clibrary.zarray_copy

def zarray_copy_subset(*args):
  return _apriltags_clibrary.zarray_copy_subset(*args)
zarray_copy_subset = _apriltags_clibrary.zarray_copy_subset

def zarray_size(*args):
  return _apriltags_clibrary.zarray_size(*args)
zarray_size = _apriltags_clibrary.zarray_size

def zarray_isempty(*args):
  return _apriltags_clibrary.zarray_isempty(*args)
zarray_isempty = _apriltags_clibrary.zarray_isempty

def zarray_ensure_capacity(*args):
  return _apriltags_clibrary.zarray_ensure_capacity(*args)
zarray_ensure_capacity = _apriltags_clibrary.zarray_ensure_capacity

def zarray_add(*args):
  return _apriltags_clibrary.zarray_add(*args)
zarray_add = _apriltags_clibrary.zarray_add

def zarray_get(*args):
  return _apriltags_clibrary.zarray_get(*args)
zarray_get = _apriltags_clibrary.zarray_get

def zarray_get_volatile(*args):
  return _apriltags_clibrary.zarray_get_volatile(*args)
zarray_get_volatile = _apriltags_clibrary.zarray_get_volatile

def zarray_copy_data(*args):
  return _apriltags_clibrary.zarray_copy_data(*args)
zarray_copy_data = _apriltags_clibrary.zarray_copy_data

def zarray_remove_value(*args):
  return _apriltags_clibrary.zarray_remove_value(*args)
zarray_remove_value = _apriltags_clibrary.zarray_remove_value

def zarray_remove_index(*args):
  return _apriltags_clibrary.zarray_remove_index(*args)
zarray_remove_index = _apriltags_clibrary.zarray_remove_index

def zarray_insert(*args):
  return _apriltags_clibrary.zarray_insert(*args)
zarray_insert = _apriltags_clibrary.zarray_insert

def zarray_set(*args):
  return _apriltags_clibrary.zarray_set(*args)
zarray_set = _apriltags_clibrary.zarray_set

def zarray_map(*args):
  return _apriltags_clibrary.zarray_map(*args)
zarray_map = _apriltags_clibrary.zarray_map

def zarray_vmap(*args):
  return _apriltags_clibrary.zarray_vmap(*args)
zarray_vmap = _apriltags_clibrary.zarray_vmap

def zarray_clear(*args):
  return _apriltags_clibrary.zarray_clear(*args)
zarray_clear = _apriltags_clibrary.zarray_clear

def zarray_contains(*args):
  return _apriltags_clibrary.zarray_contains(*args)
zarray_contains = _apriltags_clibrary.zarray_contains

def zarray_sort(*args):
  return _apriltags_clibrary.zarray_sort(*args)
zarray_sort = _apriltags_clibrary.zarray_sort

def zstrcmp(*args):
  return _apriltags_clibrary.zstrcmp(*args)
zstrcmp = _apriltags_clibrary.zstrcmp

def zarray_index_of(*args):
  return _apriltags_clibrary.zarray_index_of(*args)
zarray_index_of = _apriltags_clibrary.zarray_index_of

def zarray_add_all(*args):
  return _apriltags_clibrary.zarray_add_all(*args)
zarray_add_all = _apriltags_clibrary.zarray_add_all
class image_u8(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, image_u8, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, image_u8, name)
    __repr__ = _swig_repr
    __swig_getmethods__["width"] = _apriltags_clibrary.image_u8_width_get
    if _newclass:width = _swig_property(_apriltags_clibrary.image_u8_width_get)
    __swig_getmethods__["height"] = _apriltags_clibrary.image_u8_height_get
    if _newclass:height = _swig_property(_apriltags_clibrary.image_u8_height_get)
    __swig_getmethods__["stride"] = _apriltags_clibrary.image_u8_stride_get
    if _newclass:stride = _swig_property(_apriltags_clibrary.image_u8_stride_get)
    __swig_getmethods__["buf"] = _apriltags_clibrary.image_u8_buf_get
    if _newclass:buf = _swig_property(_apriltags_clibrary.image_u8_buf_get)
    def __init__(self): 
        this = _apriltags_clibrary.new_image_u8()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_image_u8
    __del__ = lambda self : None;
image_u8_swigregister = _apriltags_clibrary.image_u8_swigregister
image_u8_swigregister(image_u8)

class image_u8_lut(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, image_u8_lut, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, image_u8_lut, name)
    __repr__ = _swig_repr
    __swig_setmethods__["scale"] = _apriltags_clibrary.image_u8_lut_scale_set
    __swig_getmethods__["scale"] = _apriltags_clibrary.image_u8_lut_scale_get
    if _newclass:scale = _swig_property(_apriltags_clibrary.image_u8_lut_scale_get, _apriltags_clibrary.image_u8_lut_scale_set)
    __swig_setmethods__["nvalues"] = _apriltags_clibrary.image_u8_lut_nvalues_set
    __swig_getmethods__["nvalues"] = _apriltags_clibrary.image_u8_lut_nvalues_get
    if _newclass:nvalues = _swig_property(_apriltags_clibrary.image_u8_lut_nvalues_get, _apriltags_clibrary.image_u8_lut_nvalues_set)
    __swig_setmethods__["values"] = _apriltags_clibrary.image_u8_lut_values_set
    __swig_getmethods__["values"] = _apriltags_clibrary.image_u8_lut_values_get
    if _newclass:values = _swig_property(_apriltags_clibrary.image_u8_lut_values_get, _apriltags_clibrary.image_u8_lut_values_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_image_u8_lut()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_image_u8_lut
    __del__ = lambda self : None;
image_u8_lut_swigregister = _apriltags_clibrary.image_u8_lut_swigregister
image_u8_lut_swigregister(image_u8_lut)


def image_u8_create(*args):
  return _apriltags_clibrary.image_u8_create(*args)
image_u8_create = _apriltags_clibrary.image_u8_create

def image_u8_create_alignment(*args):
  return _apriltags_clibrary.image_u8_create_alignment(*args)
image_u8_create_alignment = _apriltags_clibrary.image_u8_create_alignment

def image_u8_create_from_f32(*args):
  return _apriltags_clibrary.image_u8_create_from_f32(*args)
image_u8_create_from_f32 = _apriltags_clibrary.image_u8_create_from_f32

def image_u8_create_from_pnm(*args):
  return _apriltags_clibrary.image_u8_create_from_pnm(*args)
image_u8_create_from_pnm = _apriltags_clibrary.image_u8_create_from_pnm

def image_u8_copy(*args):
  return _apriltags_clibrary.image_u8_copy(*args)
image_u8_copy = _apriltags_clibrary.image_u8_copy

def image_u8_draw_line(*args):
  return _apriltags_clibrary.image_u8_draw_line(*args)
image_u8_draw_line = _apriltags_clibrary.image_u8_draw_line

def image_u8_draw_circle(*args):
  return _apriltags_clibrary.image_u8_draw_circle(*args)
image_u8_draw_circle = _apriltags_clibrary.image_u8_draw_circle

def image_u8_draw_annulus(*args):
  return _apriltags_clibrary.image_u8_draw_annulus(*args)
image_u8_draw_annulus = _apriltags_clibrary.image_u8_draw_annulus

def image_u8_fill_line_max(*args):
  return _apriltags_clibrary.image_u8_fill_line_max(*args)
image_u8_fill_line_max = _apriltags_clibrary.image_u8_fill_line_max

def image_u8_darken(*args):
  return _apriltags_clibrary.image_u8_darken(*args)
image_u8_darken = _apriltags_clibrary.image_u8_darken

def image_u8_gaussian_blur(*args):
  return _apriltags_clibrary.image_u8_gaussian_blur(*args)
image_u8_gaussian_blur = _apriltags_clibrary.image_u8_gaussian_blur

def image_u8_decimate(*args):
  return _apriltags_clibrary.image_u8_decimate(*args)
image_u8_decimate = _apriltags_clibrary.image_u8_decimate

def image_u8_destroy(*args):
  return _apriltags_clibrary.image_u8_destroy(*args)
image_u8_destroy = _apriltags_clibrary.image_u8_destroy

def image_u8_write_pnm(*args):
  return _apriltags_clibrary.image_u8_write_pnm(*args)
image_u8_write_pnm = _apriltags_clibrary.image_u8_write_pnm

def image_u8_rotate(*args):
  return _apriltags_clibrary.image_u8_rotate(*args)
image_u8_rotate = _apriltags_clibrary.image_u8_rotate
APRILTAG_TASKS_PER_THREAD_TARGET = _apriltags_clibrary.APRILTAG_TASKS_PER_THREAD_TARGET
class quad(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, quad, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, quad, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p"] = _apriltags_clibrary.quad_p_set
    __swig_getmethods__["p"] = _apriltags_clibrary.quad_p_get
    if _newclass:p = _swig_property(_apriltags_clibrary.quad_p_get, _apriltags_clibrary.quad_p_set)
    __swig_setmethods__["H"] = _apriltags_clibrary.quad_H_set
    __swig_getmethods__["H"] = _apriltags_clibrary.quad_H_get
    if _newclass:H = _swig_property(_apriltags_clibrary.quad_H_get, _apriltags_clibrary.quad_H_set)
    __swig_setmethods__["Hinv"] = _apriltags_clibrary.quad_Hinv_set
    __swig_getmethods__["Hinv"] = _apriltags_clibrary.quad_Hinv_get
    if _newclass:Hinv = _swig_property(_apriltags_clibrary.quad_Hinv_get, _apriltags_clibrary.quad_Hinv_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_quad()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_quad
    __del__ = lambda self : None;
quad_swigregister = _apriltags_clibrary.quad_swigregister
quad_swigregister(quad)

class apriltag_family(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apriltag_family, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apriltag_family, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ncodes"] = _apriltags_clibrary.apriltag_family_ncodes_set
    __swig_getmethods__["ncodes"] = _apriltags_clibrary.apriltag_family_ncodes_get
    if _newclass:ncodes = _swig_property(_apriltags_clibrary.apriltag_family_ncodes_get, _apriltags_clibrary.apriltag_family_ncodes_set)
    __swig_setmethods__["codes"] = _apriltags_clibrary.apriltag_family_codes_set
    __swig_getmethods__["codes"] = _apriltags_clibrary.apriltag_family_codes_get
    if _newclass:codes = _swig_property(_apriltags_clibrary.apriltag_family_codes_get, _apriltags_clibrary.apriltag_family_codes_set)
    __swig_setmethods__["black_border"] = _apriltags_clibrary.apriltag_family_black_border_set
    __swig_getmethods__["black_border"] = _apriltags_clibrary.apriltag_family_black_border_get
    if _newclass:black_border = _swig_property(_apriltags_clibrary.apriltag_family_black_border_get, _apriltags_clibrary.apriltag_family_black_border_set)
    __swig_setmethods__["d"] = _apriltags_clibrary.apriltag_family_d_set
    __swig_getmethods__["d"] = _apriltags_clibrary.apriltag_family_d_get
    if _newclass:d = _swig_property(_apriltags_clibrary.apriltag_family_d_get, _apriltags_clibrary.apriltag_family_d_set)
    __swig_setmethods__["h"] = _apriltags_clibrary.apriltag_family_h_set
    __swig_getmethods__["h"] = _apriltags_clibrary.apriltag_family_h_get
    if _newclass:h = _swig_property(_apriltags_clibrary.apriltag_family_h_get, _apriltags_clibrary.apriltag_family_h_set)
    __swig_setmethods__["name"] = _apriltags_clibrary.apriltag_family_name_set
    __swig_getmethods__["name"] = _apriltags_clibrary.apriltag_family_name_get
    if _newclass:name = _swig_property(_apriltags_clibrary.apriltag_family_name_get, _apriltags_clibrary.apriltag_family_name_set)
    __swig_setmethods__["impl"] = _apriltags_clibrary.apriltag_family_impl_set
    __swig_getmethods__["impl"] = _apriltags_clibrary.apriltag_family_impl_get
    if _newclass:impl = _swig_property(_apriltags_clibrary.apriltag_family_impl_get, _apriltags_clibrary.apriltag_family_impl_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_apriltag_family()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_apriltag_family
    __del__ = lambda self : None;
apriltag_family_swigregister = _apriltags_clibrary.apriltag_family_swigregister
apriltag_family_swigregister(apriltag_family)

class apriltag_quad_thresh_params(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apriltag_quad_thresh_params, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apriltag_quad_thresh_params, name)
    __repr__ = _swig_repr
    __swig_setmethods__["min_cluster_pixels"] = _apriltags_clibrary.apriltag_quad_thresh_params_min_cluster_pixels_set
    __swig_getmethods__["min_cluster_pixels"] = _apriltags_clibrary.apriltag_quad_thresh_params_min_cluster_pixels_get
    if _newclass:min_cluster_pixels = _swig_property(_apriltags_clibrary.apriltag_quad_thresh_params_min_cluster_pixels_get, _apriltags_clibrary.apriltag_quad_thresh_params_min_cluster_pixels_set)
    __swig_setmethods__["max_nmaxima"] = _apriltags_clibrary.apriltag_quad_thresh_params_max_nmaxima_set
    __swig_getmethods__["max_nmaxima"] = _apriltags_clibrary.apriltag_quad_thresh_params_max_nmaxima_get
    if _newclass:max_nmaxima = _swig_property(_apriltags_clibrary.apriltag_quad_thresh_params_max_nmaxima_get, _apriltags_clibrary.apriltag_quad_thresh_params_max_nmaxima_set)
    __swig_setmethods__["critical_rad"] = _apriltags_clibrary.apriltag_quad_thresh_params_critical_rad_set
    __swig_getmethods__["critical_rad"] = _apriltags_clibrary.apriltag_quad_thresh_params_critical_rad_get
    if _newclass:critical_rad = _swig_property(_apriltags_clibrary.apriltag_quad_thresh_params_critical_rad_get, _apriltags_clibrary.apriltag_quad_thresh_params_critical_rad_set)
    __swig_setmethods__["max_line_fit_mse"] = _apriltags_clibrary.apriltag_quad_thresh_params_max_line_fit_mse_set
    __swig_getmethods__["max_line_fit_mse"] = _apriltags_clibrary.apriltag_quad_thresh_params_max_line_fit_mse_get
    if _newclass:max_line_fit_mse = _swig_property(_apriltags_clibrary.apriltag_quad_thresh_params_max_line_fit_mse_get, _apriltags_clibrary.apriltag_quad_thresh_params_max_line_fit_mse_set)
    __swig_setmethods__["min_white_black_diff"] = _apriltags_clibrary.apriltag_quad_thresh_params_min_white_black_diff_set
    __swig_getmethods__["min_white_black_diff"] = _apriltags_clibrary.apriltag_quad_thresh_params_min_white_black_diff_get
    if _newclass:min_white_black_diff = _swig_property(_apriltags_clibrary.apriltag_quad_thresh_params_min_white_black_diff_get, _apriltags_clibrary.apriltag_quad_thresh_params_min_white_black_diff_set)
    __swig_setmethods__["deglitch"] = _apriltags_clibrary.apriltag_quad_thresh_params_deglitch_set
    __swig_getmethods__["deglitch"] = _apriltags_clibrary.apriltag_quad_thresh_params_deglitch_get
    if _newclass:deglitch = _swig_property(_apriltags_clibrary.apriltag_quad_thresh_params_deglitch_get, _apriltags_clibrary.apriltag_quad_thresh_params_deglitch_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_apriltag_quad_thresh_params()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_apriltag_quad_thresh_params
    __del__ = lambda self : None;
apriltag_quad_thresh_params_swigregister = _apriltags_clibrary.apriltag_quad_thresh_params_swigregister
apriltag_quad_thresh_params_swigregister(apriltag_quad_thresh_params)

class apriltag_detector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apriltag_detector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apriltag_detector, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nthreads"] = _apriltags_clibrary.apriltag_detector_nthreads_set
    __swig_getmethods__["nthreads"] = _apriltags_clibrary.apriltag_detector_nthreads_get
    if _newclass:nthreads = _swig_property(_apriltags_clibrary.apriltag_detector_nthreads_get, _apriltags_clibrary.apriltag_detector_nthreads_set)
    __swig_setmethods__["quad_decimate"] = _apriltags_clibrary.apriltag_detector_quad_decimate_set
    __swig_getmethods__["quad_decimate"] = _apriltags_clibrary.apriltag_detector_quad_decimate_get
    if _newclass:quad_decimate = _swig_property(_apriltags_clibrary.apriltag_detector_quad_decimate_get, _apriltags_clibrary.apriltag_detector_quad_decimate_set)
    __swig_setmethods__["quad_sigma"] = _apriltags_clibrary.apriltag_detector_quad_sigma_set
    __swig_getmethods__["quad_sigma"] = _apriltags_clibrary.apriltag_detector_quad_sigma_get
    if _newclass:quad_sigma = _swig_property(_apriltags_clibrary.apriltag_detector_quad_sigma_get, _apriltags_clibrary.apriltag_detector_quad_sigma_set)
    __swig_setmethods__["refine_decode"] = _apriltags_clibrary.apriltag_detector_refine_decode_set
    __swig_getmethods__["refine_decode"] = _apriltags_clibrary.apriltag_detector_refine_decode_get
    if _newclass:refine_decode = _swig_property(_apriltags_clibrary.apriltag_detector_refine_decode_get, _apriltags_clibrary.apriltag_detector_refine_decode_set)
    __swig_setmethods__["refine_pose"] = _apriltags_clibrary.apriltag_detector_refine_pose_set
    __swig_getmethods__["refine_pose"] = _apriltags_clibrary.apriltag_detector_refine_pose_get
    if _newclass:refine_pose = _swig_property(_apriltags_clibrary.apriltag_detector_refine_pose_get, _apriltags_clibrary.apriltag_detector_refine_pose_set)
    __swig_setmethods__["debug"] = _apriltags_clibrary.apriltag_detector_debug_set
    __swig_getmethods__["debug"] = _apriltags_clibrary.apriltag_detector_debug_get
    if _newclass:debug = _swig_property(_apriltags_clibrary.apriltag_detector_debug_get, _apriltags_clibrary.apriltag_detector_debug_set)
    __swig_setmethods__["qtp"] = _apriltags_clibrary.apriltag_detector_qtp_set
    __swig_getmethods__["qtp"] = _apriltags_clibrary.apriltag_detector_qtp_get
    if _newclass:qtp = _swig_property(_apriltags_clibrary.apriltag_detector_qtp_get, _apriltags_clibrary.apriltag_detector_qtp_set)
    __swig_setmethods__["tp"] = _apriltags_clibrary.apriltag_detector_tp_set
    __swig_getmethods__["tp"] = _apriltags_clibrary.apriltag_detector_tp_get
    if _newclass:tp = _swig_property(_apriltags_clibrary.apriltag_detector_tp_get, _apriltags_clibrary.apriltag_detector_tp_set)
    __swig_setmethods__["nedges"] = _apriltags_clibrary.apriltag_detector_nedges_set
    __swig_getmethods__["nedges"] = _apriltags_clibrary.apriltag_detector_nedges_get
    if _newclass:nedges = _swig_property(_apriltags_clibrary.apriltag_detector_nedges_get, _apriltags_clibrary.apriltag_detector_nedges_set)
    __swig_setmethods__["nsegments"] = _apriltags_clibrary.apriltag_detector_nsegments_set
    __swig_getmethods__["nsegments"] = _apriltags_clibrary.apriltag_detector_nsegments_get
    if _newclass:nsegments = _swig_property(_apriltags_clibrary.apriltag_detector_nsegments_get, _apriltags_clibrary.apriltag_detector_nsegments_set)
    __swig_setmethods__["nquads"] = _apriltags_clibrary.apriltag_detector_nquads_set
    __swig_getmethods__["nquads"] = _apriltags_clibrary.apriltag_detector_nquads_get
    if _newclass:nquads = _swig_property(_apriltags_clibrary.apriltag_detector_nquads_get, _apriltags_clibrary.apriltag_detector_nquads_set)
    __swig_setmethods__["tag_families"] = _apriltags_clibrary.apriltag_detector_tag_families_set
    __swig_getmethods__["tag_families"] = _apriltags_clibrary.apriltag_detector_tag_families_get
    if _newclass:tag_families = _swig_property(_apriltags_clibrary.apriltag_detector_tag_families_get, _apriltags_clibrary.apriltag_detector_tag_families_set)
    __swig_setmethods__["wp"] = _apriltags_clibrary.apriltag_detector_wp_set
    __swig_getmethods__["wp"] = _apriltags_clibrary.apriltag_detector_wp_get
    if _newclass:wp = _swig_property(_apriltags_clibrary.apriltag_detector_wp_get, _apriltags_clibrary.apriltag_detector_wp_set)
    __swig_setmethods__["mutex"] = _apriltags_clibrary.apriltag_detector_mutex_set
    __swig_getmethods__["mutex"] = _apriltags_clibrary.apriltag_detector_mutex_get
    if _newclass:mutex = _swig_property(_apriltags_clibrary.apriltag_detector_mutex_get, _apriltags_clibrary.apriltag_detector_mutex_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_apriltag_detector()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_apriltag_detector
    __del__ = lambda self : None;
apriltag_detector_swigregister = _apriltags_clibrary.apriltag_detector_swigregister
apriltag_detector_swigregister(apriltag_detector)

class apriltag_detection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, apriltag_detection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, apriltag_detection, name)
    __repr__ = _swig_repr
    __swig_setmethods__["family"] = _apriltags_clibrary.apriltag_detection_family_set
    __swig_getmethods__["family"] = _apriltags_clibrary.apriltag_detection_family_get
    if _newclass:family = _swig_property(_apriltags_clibrary.apriltag_detection_family_get, _apriltags_clibrary.apriltag_detection_family_set)
    __swig_setmethods__["id"] = _apriltags_clibrary.apriltag_detection_id_set
    __swig_getmethods__["id"] = _apriltags_clibrary.apriltag_detection_id_get
    if _newclass:id = _swig_property(_apriltags_clibrary.apriltag_detection_id_get, _apriltags_clibrary.apriltag_detection_id_set)
    __swig_setmethods__["hamming"] = _apriltags_clibrary.apriltag_detection_hamming_set
    __swig_getmethods__["hamming"] = _apriltags_clibrary.apriltag_detection_hamming_get
    if _newclass:hamming = _swig_property(_apriltags_clibrary.apriltag_detection_hamming_get, _apriltags_clibrary.apriltag_detection_hamming_set)
    __swig_setmethods__["goodness"] = _apriltags_clibrary.apriltag_detection_goodness_set
    __swig_getmethods__["goodness"] = _apriltags_clibrary.apriltag_detection_goodness_get
    if _newclass:goodness = _swig_property(_apriltags_clibrary.apriltag_detection_goodness_get, _apriltags_clibrary.apriltag_detection_goodness_set)
    __swig_setmethods__["decision_margin"] = _apriltags_clibrary.apriltag_detection_decision_margin_set
    __swig_getmethods__["decision_margin"] = _apriltags_clibrary.apriltag_detection_decision_margin_get
    if _newclass:decision_margin = _swig_property(_apriltags_clibrary.apriltag_detection_decision_margin_get, _apriltags_clibrary.apriltag_detection_decision_margin_set)
    __swig_setmethods__["H"] = _apriltags_clibrary.apriltag_detection_H_set
    __swig_getmethods__["H"] = _apriltags_clibrary.apriltag_detection_H_get
    if _newclass:H = _swig_property(_apriltags_clibrary.apriltag_detection_H_get, _apriltags_clibrary.apriltag_detection_H_set)
    __swig_setmethods__["c"] = _apriltags_clibrary.apriltag_detection_c_set
    __swig_getmethods__["c"] = _apriltags_clibrary.apriltag_detection_c_get
    if _newclass:c = _swig_property(_apriltags_clibrary.apriltag_detection_c_get, _apriltags_clibrary.apriltag_detection_c_set)
    __swig_setmethods__["p"] = _apriltags_clibrary.apriltag_detection_p_set
    __swig_getmethods__["p"] = _apriltags_clibrary.apriltag_detection_p_get
    if _newclass:p = _swig_property(_apriltags_clibrary.apriltag_detection_p_get, _apriltags_clibrary.apriltag_detection_p_set)
    def __init__(self): 
        this = _apriltags_clibrary.new_apriltag_detection()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _apriltags_clibrary.delete_apriltag_detection
    __del__ = lambda self : None;
apriltag_detection_swigregister = _apriltags_clibrary.apriltag_detection_swigregister
apriltag_detection_swigregister(apriltag_detection)


def apriltag_detector_create():
  return _apriltags_clibrary.apriltag_detector_create()
apriltag_detector_create = _apriltags_clibrary.apriltag_detector_create

def apriltag_detector_add_family(*args):
  return _apriltags_clibrary.apriltag_detector_add_family(*args)
apriltag_detector_add_family = _apriltags_clibrary.apriltag_detector_add_family

def apriltag_detector_remove_family(*args):
  return _apriltags_clibrary.apriltag_detector_remove_family(*args)
apriltag_detector_remove_family = _apriltags_clibrary.apriltag_detector_remove_family

def apriltag_detector_clear_families(*args):
  return _apriltags_clibrary.apriltag_detector_clear_families(*args)
apriltag_detector_clear_families = _apriltags_clibrary.apriltag_detector_clear_families

def apriltag_detector_destroy(*args):
  return _apriltags_clibrary.apriltag_detector_destroy(*args)
apriltag_detector_destroy = _apriltags_clibrary.apriltag_detector_destroy

def apriltag_detector_detect(*args):
  return _apriltags_clibrary.apriltag_detector_detect(*args)
apriltag_detector_detect = _apriltags_clibrary.apriltag_detector_detect

def apriltag_detection_destroy(*args):
  return _apriltags_clibrary.apriltag_detection_destroy(*args)
apriltag_detection_destroy = _apriltags_clibrary.apriltag_detection_destroy

def tag36h11_create():
  return _apriltags_clibrary.tag36h11_create()
tag36h11_create = _apriltags_clibrary.tag36h11_create

def tag36h11_destroy(*args):
  return _apriltags_clibrary.tag36h11_destroy(*args)
tag36h11_destroy = _apriltags_clibrary.tag36h11_destroy

def cdata(*args):
  return _apriltags_clibrary.cdata(*args)
cdata = _apriltags_clibrary.cdata

def memmove(*args):
  return _apriltags_clibrary.memmove(*args)
memmove = _apriltags_clibrary.memmove

def ARNerve_GetDetection(*args):
  return _apriltags_clibrary.ARNerve_GetDetection(*args)
ARNerve_GetDetection = _apriltags_clibrary.ARNerve_GetDetection

def ARNerve_GetDetection_Coord_X(*args):
  return _apriltags_clibrary.ARNerve_GetDetection_Coord_X(*args)
ARNerve_GetDetection_Coord_X = _apriltags_clibrary.ARNerve_GetDetection_Coord_X

def ARNerve_GetDetection_Coord_Y(*args):
  return _apriltags_clibrary.ARNerve_GetDetection_Coord_Y(*args)
ARNerve_GetDetection_Coord_Y = _apriltags_clibrary.ARNerve_GetDetection_Coord_Y

def ARNerve_Imageu8_GetWidth(*args):
  return _apriltags_clibrary.ARNerve_Imageu8_GetWidth(*args)
ARNerve_Imageu8_GetWidth = _apriltags_clibrary.ARNerve_Imageu8_GetWidth

def ARNerve_Imageu8_GetHeight(*args):
  return _apriltags_clibrary.ARNerve_Imageu8_GetHeight(*args)
ARNerve_Imageu8_GetHeight = _apriltags_clibrary.ARNerve_Imageu8_GetHeight

def ARNerve_Imageu8_GetStride(*args):
  return _apriltags_clibrary.ARNerve_Imageu8_GetStride(*args)
ARNerve_Imageu8_GetStride = _apriltags_clibrary.ARNerve_Imageu8_GetStride

def ARNerve_Imageu8_GetBuffer(*args):
  return _apriltags_clibrary.ARNerve_Imageu8_GetBuffer(*args)
ARNerve_Imageu8_GetBuffer = _apriltags_clibrary.ARNerve_Imageu8_GetBuffer

def ARNerve_Imageu8_CopyToBuffer(*args):
  return _apriltags_clibrary.ARNerve_Imageu8_CopyToBuffer(*args)
ARNerve_Imageu8_CopyToBuffer = _apriltags_clibrary.ARNerve_Imageu8_CopyToBuffer
# This file is compatible with both classic and new-style classes.


