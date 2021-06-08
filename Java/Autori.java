/**
*Solution to kattis problem source: https://open.kattis.com/problems/autori
*/

import java.util.Scanner;

public class Autori {
  String rawString;
  String stringToPrint = "";

  public void handleString(){
    for (int index = 0; index < rawString.length(); index++){
      if(Character.isUpperCase(rawString.charAt(index))){
        stringToPrint += rawString.charAt(index);
      }
    }
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    rawString = kattio.next();
    kattio.close();
  }
  public void handleOutput(){
    System.out.println(stringToPrint);
  }
  public static void main(String[] args) {
    Autori thisInstance = new Autori();
    thisInstance.handleInput();
    thisInstance.handleString();
    thisInstance.handleOutput();
  }
}
