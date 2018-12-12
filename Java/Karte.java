/*
*Kattis problem solution source: https://open.kattis.com/problems/karte
*/

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Karte {
  ArrayList<Integer> values = new ArrayList<>();

  private void handleInput() {
    Scanner kattio = new Scanner(System.in);
    String theString = kattio.next();
    kattio.close();
    String toAppend = "";
    //This is the really ugly part. Essentially it reads theString and appends to an individual arraylist the "cards" for each suit.
    //I wanted to use a combination of .split and .join but couldn't get it to work properly and this turned out to be faster.
    ArrayList<String> partP = new ArrayList<>();
    ArrayList<String> partK = new ArrayList<>();
    ArrayList<String> partH = new ArrayList<>();
    ArrayList<String> partT = new ArrayList<>();
    for (int i = 0; i < theString.length(); i+=3) {
      if (theString.charAt(i)=='P') {
        toAppend = Character.toString(theString.charAt(i))+Character.toString(theString.charAt(i+1))+Character.toString(theString.charAt(i+2));
        partP.add(toAppend);
      } else if (theString.charAt(i)=='K'){
        toAppend = Character.toString(theString.charAt(i))+Character.toString(theString.charAt(i+1))+Character.toString(theString.charAt(i+2));
        partK.add(toAppend);
      } else if (theString.charAt(i)=='H'){
        toAppend = Character.toString(theString.charAt(i))+Character.toString(theString.charAt(i+1))+Character.toString(theString.charAt(i+2));
        partH.add(toAppend);
      } else if (theString.charAt(i)=='T'){
      toAppend = Character.toString(theString.charAt(i))+Character.toString(theString.charAt(i+1))+Character.toString(theString.charAt(i+2));
      partT.add(toAppend);
    }
  }
  //The check method  (below) converts the arraylist to a hashset, this removes duplicates therefor if the size of set < list there where duplicates and check outputs GRESKA and return true so it will break and only output once.
  if (check(partP)) {
  } else if (check(partK)) {
  } else if (check(partH)) {
  } else if (check(partT)) {
  } else {
    handleOutput(values);
  }
}

  private boolean check(ArrayList myList) {
    Set<Integer> set = new HashSet<Integer>(myList);
    if (myList.size() > set.size()) {
      System.out.println("GRESKA");
      return true;
    } else {
      values.add(13-set.size());
    }
    return false;
  }


  private void handleOutput (ArrayList s) {
    System.out.println(s.get(0)+" "+s.get(1)+" "+s.get(2)+" "+s.get(3));
  }

  public static void main(String[] args) {
    Karte thisInstance = new Karte();
    thisInstance.handleInput();
  }
}
