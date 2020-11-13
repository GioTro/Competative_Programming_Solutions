/**
Solution to kattis problem source: https://open.kattis.com/problems/tarifa
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Pero {
  private int initialValue;
  private int nMonths;
  private ArrayList<Integer> usage = new ArrayList<Integer>();
  private int total;


  public void turboCalculator(){
    total = initialValue;
    for (int index = 0; index < (nMonths); index++){
      total -= usage.get(index);
      total += initialValue;
    }
    //output
    System.out.println(total);
  }
  public void handleInput(){
    Scanner kattio = new Scanner(System.in);
    initialValue = kattio.nextInt();
    nMonths = kattio.nextInt();
    for (int i = 0; i < (nMonths); i++){
      usage.add(kattio.nextInt());
    }
    kattio.close();
  }
  public static void main(String[] args) {
    Pero thisInstance = new Pero();
    thisInstance.handleInput();
    thisInstance.turboCalculator();
  }
}
