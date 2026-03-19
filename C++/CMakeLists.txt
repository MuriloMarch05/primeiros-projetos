cmake_minimum_required(VERSION 4.1)
project(C__)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories("Aula 5")

add_executable(C__
        "Aula 5/ex04.cpp"
        helloworld.cpp
        multiplicacao.cpp)
