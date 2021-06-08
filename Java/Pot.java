/**
*Solution to kattis problem source: https://open.kattis.com/problems/pot
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Pot {
  private int number, total;
  private ArrayList<Integer> numbers = new ArrayList<Integer>();
  private ArrayList<String> strings = new ArrayList<String>();


//Performs the calculation
  public void calculator(){
    for (int i = 0; i<number; i++) {
      total += (int) Math.pow(numbers.get(i) , numbers.get(i+number));
    }
  }
//Takes a string of numbers and returns an integer that is  either the last digit or the first digits depending on the boolean.
  public int parse(String argument, Boolean lastOr){
    int returnValue = 0;
    if (lastOr == false) {
      returnValue = Integer.parseInt(argument.substring(0, argument.length()-1));
    }
    if (lastOr == true){
      returnValue = Integer.parseInt(argument.substring(argument.length()-1));
    }
    return returnValue;
  }

  public void firstNumbers() {
    for (int i = 0; i < number; i++){
      numbers.add(parse(strings.get(i), false));
    }
  }
  public void lastNumbers() {
    for (int i = 0; i < number; i++){
      numbers.add(parse(strings.get(i), true));
    }
  }

  public void handleInput() {
  Scanner kattio = new Scanner(System.in);
  number = kattio.nextInt();
  for (int index = 0; index < number; index++) {
    strings.add(Integer.toString(kattio.nextInt()));
  }
  kattio.close();
  }
  
  public void handleOutput() {
    System.out.println(total);
  }
  public static void main(String[] args) {
    Pot thisInstance = new Pot();
    thisInstance.handleInput();
    thisInstance.firstNumbers();
    thisInstance.lastNumbers();
    thisInstance.calculator();
    thisInstance.handleOutput();

  }

}
