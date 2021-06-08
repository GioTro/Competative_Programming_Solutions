/**
*Solution for kattis problem source: https://open.kattis.com/problems/aaah
*/

import java.util.Scanner;

class Aaah {
  public void handleInput(){
    Scanner kattio = new Scanner(System.in);
    String first = kattio.nextLine();
    String second = kattio.nextLine();
    kattio.close();
    handleOutput(first, second);
  }
  public void handleOutput(String first, String second) {
    if (first.length() >= second.length()) {
      System.out.println("go");
    } else {
      System.out.println("no");
    }
  }
  public static void main(String[] args) {
    Aaah thisInstance = new Aaah();
    thisInstance.handleInput();
  }
}
