/**
*Solution to Kattis Problem source: https://open.kattis.com/problems/twostones
*/

import java.util.Scanner;

public class Twostones {
  int nStones, winner;

  public void mod(){
    winner = nStones % 2;
    this.handleOutput();
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    nStones = kattio.nextInt();
    kattio.close();
    this.mod();
  }
  public void handleOutput(){
    if (winner == 1){
      System.out.println("Alice");
    }
    if (winner == 0) {
      System.out.println("Bob");
    }
  }

  public static void main(String[] args){
    Twostones thisInstance = new Twostones();
    thisInstance.handleInput();
  }
}
