/*
*Solution to Kattis problem source: https://open.kattis.com/problems/modulo
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Modulo {
  private ArrayList<Integer> numbers = new ArrayList<Integer>();
  private ArrayList<Integer> modulo = new ArrayList<Integer>();
  private ArrayList<Integer> distinct = new ArrayList<Integer>();
  private int mod, check;
  private int unique = 0;

  public void count(){
    for (int index = 0; index < numbers.size(); index++){
      int mod = numbers.get(index) % 42;
      modulo.add(mod);
    }
    for (int index = 0; index < numbers.size(); index++){
      int check = modulo.get(index);
      if(!(distinct.contains(check))) {
        distinct.add(check);
      }
    }
  modulo = null;
  numbers = null;
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    for (int index = 0; index < 10; index++){
      numbers.add(kattio.nextInt());
    }
    kattio.close();
  }
  public void handleOutput(){
    unique = distinct.size();
    System.out.println(unique);
  }
  public static void main(String[] args){
    Modulo thisInstance = new Modulo();
    thisInstance.handleInput();
    thisInstance.count();
    thisInstance.handleOutput();
  }
}
