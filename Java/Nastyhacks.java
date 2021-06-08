/**
Solution for kattis problem source: https://open.kattis.com/problems/nastyhacks
*/

import java.util.Scanner;
import java.util.ArrayList;

public class Nastyhacks{
  private int index;
    private int cases;
    private ArrayList<Integer> numbers = new ArrayList<Integer>();
    private ArrayList<Integer> ad = new ArrayList<Integer>();
    private ArrayList<Integer> noAd = new ArrayList<Integer>();



  public void revenue() {
    int count = 1;
    int total = 0;
    int fixed = 0;
    for (int i = 0; i < index; i++){
      total = numbers.get(count) - numbers.get(count+1);
      fixed = numbers.get(count - 1);
      ad.add(total);
      noAd.add(fixed);
      count += 3;
    }
    numbers = null;
  }

  public void handleInput(){
    Scanner kattio = new Scanner(System.in);
    index = kattio.nextInt();
    cases = index*3;
    for (int i = 0; i < (cases); i++){
      numbers.add(kattio.nextInt());
    }
    kattio.close();
  }
  public void handleOutput(){
    for (int i = 0; i < index; i++){
      if (ad.get(i) > noAd.get(i)) {
        System.out.println("advertise");
      }
      if ( ad.get(i) == noAd.get(i) ) {
        System.out.println("does not matter");
      }
      if (ad.get(i) < noAd.get(i)) {
        System.out.println("do not advertise");
      }
    }
  }

  public static void main(String[] args){
    Nastyhacks thisInstance = new Nastyhacks();
    thisInstance.handleInput();
    thisInstance.revenue();
    thisInstance.handleOutput();
  }
}
