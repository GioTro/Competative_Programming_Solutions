/**
Solution for kattis problem source: https://open.kattis.com/problems/carrots
*/

import java.util.Scanner;

public class Carrots {
  public static void main(String[] args){
    int carrots = 0;
    Scanner kattio = new Scanner(System.in);
    while (kattio.hasNextInt()) {
      carrots = kattio.nextInt();
    }
    kattio.close();
    System.out.println(carrots);
  }
}
