#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main(){
	float coeff;
	float constTerm;
	float sum_xy;
	float sum_x;
	float sum_y;
	float sum_x_square;
	float sum_y_square;

    coeff = 0;
    constTerm = 0;
    sum_y = 0;
    sum_y_square = 0;
    sum_x_square = 0;
    sum_x = 0;
    int N = 4;
    vector<float> xi = {1,2,3,4};
    vector<float> yi = {1,2,3,4};
    cout << xi[1];

    for (int i = 0; i < N; i++) {
        // In a csv file all the values of
        // xi and yi are separated by commas
        sum_xy += xi[i] * yi[i];
        sum_x += xi[i];
        sum_y += yi[i];
        sum_x_square += xi[i] * xi[i];
        sum_y_square += yi[i] * yi[i];
    }
    coeff = (N * sum_xy - sum_x * sum_y) / (N * sum_x_square - sum_x * sum_x);		
    constTerm = (sum_y * sum_x_square - sum_x * sum_xy) / (N * sum_x_square - sum_x * sum_x);
    cout << "The best fitting line is y = "	<< coeff << "x + " << constTerm << endl;

}