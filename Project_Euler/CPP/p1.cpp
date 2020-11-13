//Sums all multiples of 3 and 5 below "target"
//My firsrt ever C++ <3

#include<iostream>
#include<string>
#include<ctime>
using namespace std;

int main() {
  int count;
  long int target;
  long int sum;
  std::cout << "Enter target: \n";
  cin >> target;
  while (count < target-1) {
    count += 1;
    if (count % 3 == 0 || count % 5 == 0) {
      sum += count;
    }
  }
  std::cout << "The sum of all multiples of 3 and 5 below " << target << " is " << sum << "\n" << endl;
}
