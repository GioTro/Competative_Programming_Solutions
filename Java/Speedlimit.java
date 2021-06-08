/**
*Solution for Kattis problem source: https://open.kattis.com/problems/speedlimit
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Speedlimit {
  private ArrayList<Integer> speeds = new ArrayList<>();
  private ArrayList<Integer> holder = new ArrayList<>();
  private ArrayList<Integer> multiplier = new ArrayList<>();
  private ArrayList<Integer> toPrint = new ArrayList<>();
  private ArrayList<Integer> time = new ArrayList<>();

  private void calculator(){
    int start = 0;
    int index = 0;
    int toAdd = 0;
    while (start < holder.size()) {
      int limit = holder.get(start);
      for (int i=0; i < limit; i++) {
        toAdd += multiplier.get(index)*speeds.get(index);
        index ++;
      }
      toPrint.add(toAdd);
      toAdd = 0;
      start ++;
    }
    multiplier = null;
    time = null;
    speeds = null;
    holder = null;
  }
  private void fetchMultiplier(){
    int start = 0;
    int index = 0;
    while (start < holder.size()) {
      int limit = holder.get(start);
      multiplier.add(time.get(index));
      index += 1;
      for (int i=1; i < limit; i++){
        int toAdd;
        toAdd = time.get(index) - time.get(index-1);
        multiplier.add(toAdd);
        index += 1;
      }
      start += 1;
    }
  }
  private void handleInput() {
    Scanner kattio = new Scanner(System.in);
    while (true) {
      int hold = kattio.nextInt();
      if (hold == -1) {
        break;
      } else {
        holder.add(hold);
        for (int index = 0; index < hold; index++){
          speeds.add(kattio.nextInt());
          time.add(kattio.nextInt());
        }
      }
    }
  }
  private void handleOutput(){
    for (int i=0; i < toPrint.size(); i++) {
      System.out.println(toPrint.get(i)+" miles");
    }
  }
  public static void main(String[] args){
    Speedlimit thisInstance = new Speedlimit();
    thisInstance.handleInput();
    thisInstance.fetchMultiplier();
    thisInstance.calculator();
    thisInstance.handleOutput();
  }
}
