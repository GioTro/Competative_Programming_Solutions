import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

public class T9Spelling{
  ArrayList<String> strings = new ArrayList<>();
  ArrayList<String> toPrint = new ArrayList<>();
  HashMap<Character, Integer> chars = new HashMap<>();

  public void handleInput(){
    Scanner io = new Scanner(System.in);
    int limit = io.nextInt();
    for(int i = 0; i <= limit; i++){
      strings.add(io.nextLine());
    }
    hashBuilder();
    stringBuilder();
    handleOutput();
  }
  private void handleOutput() {
    for(int i = 1; i < toPrint.size(); i++) {
      System.out.println("Case #"+(i)+": "+toPrint.get(i));
    }
  }
  private void stringBuilder(){
    for(int i = 0; i < strings.size(); i++){
      String string = "";
      for(int j = 0; j < strings.get(i).length(); j++){
        if( j>0 && calculateInteger(strings.get(i).charAt(j))%10 == calculateInteger(strings.get(i).charAt(j-1))%10) {
          string+=" ";
        }
        string+= String.valueOf(calculateInteger(strings.get(i).charAt(j)));
      }
      toPrint.add(string);
    }
  }

  private Integer calculateInteger(char c) {
    return chars.get(c);
  }
  private void hashBuilder() {
    chars.put('a', 2);
    chars.put('b', 22);
    chars.put('c', 222);
    chars.put('d', 3);
    chars.put('e', 33);
    chars.put('f', 333);
    chars.put('g', 4);
    chars.put('h', 44);
    chars.put('i', 444);
    chars.put('j', 5);
    chars.put('k', 55);
    chars.put('l', 555);
    chars.put('m', 6);
    chars.put('n', 66);
    chars.put('o', 666);
    chars.put('p', 7);
    chars.put('q', 77);
    chars.put('r', 777);
    chars.put('s', 7777);
    chars.put('t', 8);
    chars.put('u', 88);
    chars.put('v', 888);
    chars.put('w', 9);
    chars.put('x', 99);
    chars.put('y', 999);
    chars.put('z', 9999);
    chars.put(' ', 0);
  }


  public static void main(String[] args) {
    T9Spelling thisInstance = new T9Spelling();
    thisInstance.handleInput();
  }
}
