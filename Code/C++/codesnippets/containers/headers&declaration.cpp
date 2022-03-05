#include <iostream>		// input/output standard library
#include <string>			// standard string library
#include <fstream>			

#include <vector>	
vector<double> v1;

#include <deque>

#include <list>	

#include <set>
set<double> s1;

#include <map>
map<double, double> m1;
multimap<double, double> mm1;

#include <unordered_set>
unordered_set<double> us1;

#include <unordered_map>	

#include<tuple>
tuple <int,char,float> tup1(20,'g',17.5);
vector<tuple<int, int, int> > v;

#include <iterator>	
#include <algorithm>	
#include <numeric>	
#include <functional>	

#include <chrono>	//measuring times

auto start = std::chrono::steady_clock::now();

	for (double i = 0; i < 10000000; i++)
	{
		//.... tings to time
	}
auto end = std::chrono::steady_clock::now();

std::chrono::duration<double> elapsed_seconds = end - start;
	