#include <iostream>
#include "functions.h"
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>


namespace py = pybind11;

size_t sum_of_elements(py::array_t<uint16_t, py::array::c_style> &array){
  size_t sum = 0;
  auto length = array.size();
  auto proxy = array.unchecked<1>();
  for(size_t i=0; i<length; ++i ){
    sum += proxy(i);
  }
  return sum;
}

py::array_t<double> convolve_2D(const py::array_t<double> &image, const py::array_t<int64_t> &kernel){

    auto _image = image.unchecked<2>();
    auto _kernel = kernel.unchecked<2>();
    auto xKernShape = _kernel.shape(0);
    auto yKernShape = _kernel.shape(1);
    auto xImgShape = _image.shape(0);
    auto yImgShape = _image.shape(1);

    auto result = py::array_t<double>({xImgShape,yImgShape});
    auto _result = result.mutable_unchecked<2>();

    for(py::ssize_t i=0; i<yImgShape-yKernShape; ++i){
        for(py::ssize_t j=0; j<xImgShape-xKernShape; ++j){
          _result(i,j) =    _kernel(0,0)*_image(i,j) 
                          + _kernel(0,1)*_image(i,j+1)
                          + _kernel(0,2)*_image(i,j+2)
                          + _kernel(1,0)*_image(i+1,j) 
                          + _kernel(1,1)*_image(i+1,j+1)
                          + _kernel(1,2)*_image(i+1,j+2)
                          + _kernel(2,0)*_image(i+2,j) 
                          + _kernel(2,1)*_image(i+2,j+1)
                          + _kernel(2,2)*_image(i+2,j+2);

        }
    }
    return result;
}



PYBIND11_MODULE(libtest, m) {

  m.def("count_primes", &count_primes, py::call_guard<py::gil_scoped_release>());
  m.def("calc_sum_of_squares", &calc_sum_of_squares, py::call_guard<py::gil_scoped_release>());
  m.def("sum_of_elements", &sum_of_elements, py::call_guard<py::gil_scoped_release>() );
  m.def("convolution_2d", &convolve_2D ,py::return_value_policy::reference_internal);
}