/**
Solution for kattis problem source: https://open.kattis.com/problems/faktor
*/

import java.util.Scanner;

public class Faktor {
  private int nArticles, faktor, total;


  public void ceilFunction(){
    for (int count = 1; count < 10000; count++ ) {
      total = (int) Math.ceil((double) count/nArticles);
      if (total == faktor) {
        total = count;
        break;
      }
    }
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    nArticles = kattio.nextInt();
    faktor = kattio.nextInt();
    kattio.close();
  }

  public void handleOutput(){
    System.out.println(total);
  }
  public static void main(String[] args){
    Faktor thisInstance = new Faktor();
    thisInstance.handleInput();
    thisInstance.ceilFunction();
    thisInstance.handleOutput();
  }
}
