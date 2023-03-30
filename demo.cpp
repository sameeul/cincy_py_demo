#include <iostream>
#include <chrono>

#include "functions.h"

int main(){
    int sample_size = 10;
    for(int i=0; i< sample_size; i++){
    auto start_time = std::chrono::high_resolution_clock::now();
    auto tmp = calc_sum_of_squares(100000000);
    //auto count = count_primes(10000);
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = end_time - start_time;
    std::cout << "elapsed time "<< std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_time).count()<< " ms" <<std::endl;

    }

}
