/**
*Solution for Kattis Problem source: https://open.kattis.com/problems/sibice
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Sibice {

  private int number, width, height, floor;
  private ArrayList<Integer> matches = new ArrayList<Integer>();

  public void fetchFloor(){
    double hold;
    hold = Math.pow(height, 2) + Math.pow(width, 2);
    hold = Math.sqrt(hold);
    floor = (int) Math.floor(hold);
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    number = kattio.nextInt();
    width = kattio.nextInt();
    height = kattio.nextInt();
    for (int i = 0; i < number; i++){
      matches.add(kattio.nextInt());
    }
    kattio.close();
  }
  public void handleOutput(){
    for (int i = 0; i < matches.size(); i++){
      if (matches.get(i) <= floor) {
        System.out.println("DA");
      } else {
        System.out.println("NE");
      }
    }
  }
  public static void main(String[] args){
    Sibice thisInstance = new Sibice();
    thisInstance.handleInput();
    thisInstance.fetchFloor();
    thisInstance.handleOutput();
  }
}
