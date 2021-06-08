/**
Solution kattis problem source: 
*/

import java.util.Scanner;
public class Rtwo{

  int r1, r2, mean;

  public void calculator() {
    r1 = mean*2 - r2;
    System.out.println(r1);

  }
  public void handleInput() {
  Scanner kattio = new Scanner(System.in);
  r2 = kattio.nextInt();
  mean = kattio.nextInt();
  kattio.close();
  }
  public static void main(String[] args){
    Rtwo thisInstance = new Rtwo();
    thisInstance.handleInput();
    thisInstance.calculator();
  }
}
