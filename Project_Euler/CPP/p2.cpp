/*
Sum all evenfibbonacci numbers under a limit value.
*/

#include<iostream>
#include<string>
#include<ctime>
using namespace std;

int main() {
  //lists are fucked up in cpp
  /*
  //Setting up
  std::list<int> sequence;
  sequence.push_back(1);
  sequence.push_back(2);
  */
  /*
  //Execution
  while (sequence.end()[-1] < limit) {
    sequence.end()[-2] + sequence.end()[-1]
  }
  */

  //using unbound variables
  //setting up

  int first = 1, second = 1, third = 0, sum = 0;
  int limit;
  std::cout << "\nSums all even fibbonacci numbers under limit. Enter limit: \n";
  cin >> limit;

  //Execution

  while (third < limit) {
    third = first + second;
    first = second;
    second = third;

    //adds to sum if current number is even.
    if (third % 2 == 0) {
      sum += third;
    }
  }

  //Prints result in terminal.
  std::cout << "\nThe sum of fibbonacci numbers under " << limit << " is " << sum << ".\n" << endl;

}
