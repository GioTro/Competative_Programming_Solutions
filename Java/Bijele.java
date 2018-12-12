/**
*Solution to kattis problem source: https://open.kattis.com/problems/bijele
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Bijele {
  private ArrayList<Integer> setPieces = new ArrayList<Integer>();
  private int[] completeSet = {1, 1, 2, 2, 2, 8};
  private int[] compare = new int[6];

  public void compare(){
    int hold;
    for (int index = 0; index < 6; index++){
      compare[index] = completeSet[index] - setPieces.get(index);
    }
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    for (int index = 0; index < 6; index++){
      setPieces.add(kattio.nextInt());
    }
    kattio.close();
  }
  public void handleOutput() {
    System.out.println(compare[0]+" "+compare[1]+" "+compare[2]+" "+compare[3]+" "+compare[4]+" "+compare[5]);
  }
  public static void main(String[] args){
    Bijele thisInstance = new Bijele();
    thisInstance.handleInput();
    thisInstance.compare();
    thisInstance.handleOutput();
  }
}
