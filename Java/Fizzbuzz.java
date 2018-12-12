/**
*Solution to kattis problem source: https://open.kattis.com/problems/fizzbuzz
*/

import java.util.Scanner;

public class Fizzbuzz {
  private int x, y;
  static int n;

  public void fizzbuzz(int number){
    String toPrint = "";
    if (number % x == 0) {
      toPrint += "Fizz";
    }
    if (number % y == 0){
      toPrint += "Buzz";
    }
    if (toPrint.length() == 0) {
      System.out.println(number);
    } else {
      System.out.println(toPrint);
    }
  }
  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    x = kattio.nextInt();
    y = kattio.nextInt();
    n = kattio.nextInt();
    kattio.close();
  }
  public static void main(String[] args){
    Fizzbuzz thisInstance = new Fizzbuzz();
    thisInstance.handleInput();
    for (int i=1; i <= n; i++){
      thisInstance.fizzbuzz(i);
    }
  }

}
