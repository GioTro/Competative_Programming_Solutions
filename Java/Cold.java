/**
*Solution to kattis problem source: https://open.kattis.com/problems/cold
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Cold {
  private int nEntries;
  private ArrayList<Integer> temperatures = new ArrayList<Integer>();
  private int counter = 0;

  public void counter(){
    for (int index = 0; index < nEntries; index++){
      if (temperatures.get(index) < 0){
        counter ++;
      }
    }

  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    nEntries = kattio.nextInt();
    for (int index = 0; index < nEntries; index++){
      temperatures.add(kattio.nextInt());
    }
    kattio.close();
  }
  public void handleOutput() {
    System.out.println(counter);
  }
  public static void main(String[] args) {
    Cold thisInstance = new Cold();
    thisInstance.handleInput();
    thisInstance.counter();
    thisInstance.handleOutput();
  }
}
