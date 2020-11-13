/**
Solution for kattis problem source:https://open.kattis.com/problems/dicecup
This is probably overcomplicating it. There has to be a better use of built in methods,
but I learned a lot doing it like this. NOTE: Not at all readable :*     :::
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Dicecup {
  private int dice1, dice2;
  private ArrayList<Integer> ways = new ArrayList<Integer>();
  private ArrayList<Integer> toPrint = new ArrayList<Integer>();

  public void ways(){
    ArrayList<Integer> total = new ArrayList<Integer>();
    for (int i = 1; i<=dice1; i++) {
      for (int j = 1; j<=dice2; j++) {
        total.add(j+i);
      }
    }
    ways = total;
  }

  public void countWays() {
    int roof = 0;
    int count = 0;
    //This loop finds how many times the element that occurs most frequently in list. Although more then one element can occur said many times.
    for (int i = 0; i<ways.size(); i++){
      int check1 = ways.get(i);
      count = 0;
      for (int j = 0; j < ways.size() ; j++){
        int check2 = ways.get(j);
        if (check2 == check1){
          count++;
        }
      if (count > roof) {
        roof = count;
        count = 0;
      }
      }
    }
    //This loop pins which sums occur "roof" times.
    for (int i = 0; i<ways.size(); i++){
      int check1 = ways.get(i);
      count = 0;
      for (int j = 0; j < ways.size() ; j++){
        int check2 = ways.get(j);
        if (check2 == check1){
          count++;
        }
        if (count == roof && !(toPrint.contains(ways.get(i)))) {
          toPrint.add(ways.get(j));
          count = 0;
        }
      }
    }
    ways = null;
    //Sorting linear. I will make my own algorithm because comparator is stupid
    //I realized I don't have to sort, because the recursion in the first for-loop dice1+dice2 =>{1*1 , 1*2 , ... , 1*dice2, 2*1, ...} will be increasing in size, so the second for-loop will pin in increasing order as it reads ways left to right.
    count = toPrint.size();
    while (count > 0) {
      for (int i = 0; i < toPrint.size()-1; i++) {
        if (toPrint.get(i+1) < toPrint.get(i)){
          int hold = toPrint.get(i);
          toPrint.set(i, toPrint.get(i+1));
          toPrint.set(i+1, hold);
          count = toPrint.size();
        } else {
          count--;
        }
      }
      count --;
    }
  }

  public void handleInput(){
    Scanner kattio = new Scanner(System.in);
    dice1 = kattio.nextInt();
    dice2 = kattio.nextInt();
    kattio.close();
  }
  public void handleOutput() {
    for (int i = 0; i<toPrint.size(); i++) {
      System.out.println(toPrint.get(i));
    }
  }
  public static void main(String[] args){
    Dicecup thisInstance = new Dicecup();
    thisInstance.handleInput();
    thisInstance.ways();
    thisInstance.countWays();
    thisInstance.handleOutput();
  }
}
