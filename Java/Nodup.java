import java.util.HashSet;
import java.util.Arrays;
import java.util.Scanner;

public class Nodup {
  public void handleInput() {
    Scanner io = new Scanner(System.in);
    String input = io.nextLine();
    String[] words = input.split("\\s+");
    io.close();
    handleOutput(words);
  }
  private void handleOutput(String[] words) {
    HashSet<String> duplicates = new HashSet<>(Arrays.asList(words));
    if(duplicates.size() != words.length) {
      System.out.println("no");
    } else {
      System.out.println("yes");
    }
  }
  public static void main(String[] args) {
    Nodup thisInstance = new Nodup();
    thisInstance.handleInput();
  }
}
