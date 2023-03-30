cmake_minimum_required(VERSION 3.20)
project(CincyPyDemo)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS_RELEASE "-O3")

set(SOURCE demo.cpp
           functions.cpp 
  )

add_executable(demo ${SOURCE})
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(libtest
                      ${SOURCE}
                      py_interface.cpp
)