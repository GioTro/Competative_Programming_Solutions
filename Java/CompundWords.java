import java.util.*;
import java.io.*;

public class CompundWords {
  ArrayList<String> words = new ArrayList<>();
  String fileName = "sample.in";

  public CompundWords() {
    handleInput();
    findCompound();
  }
  public void handleInput(){
    Scanner io = new Scanner(new BufferedInputStream(System.in));
    while(io.hasNext()){
      words.add(io.next());
    }
  }
  private void findCompound() {
    HashSet<String> toReturn = new HashSet<>();
    for(int i = 0; i < words.size(); i++){
      for(int j = 0; j < words.size(); j++){
        if(j == i){
          continue;
        } else {
          toReturn.add(words.get(i)+words.get(j));
        }
      }
    }
    ArrayList<String> toPrint = new ArrayList<>(toReturn);
    Collections.sort(toPrint);
    handleOutput(toPrint);
  }
  private void handleOutput(ArrayList<String> toPrint){
    for(String string: toPrint){
      System.out.println(string);
    }
  }
  public static void main(String[] args) {
    CompundWords instance = new CompundWords();
  }
}
