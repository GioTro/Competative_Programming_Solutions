import java.util.Scanner;

public class Conundrum {


  public void handleInput() {
    Scanner io = new Scanner(System.in);
    String input = io.nextLine();
    io.close();
    handleOutput(input);
  }
  private void handleOutput(String input) {
    char[] chars = {'P', 'E', 'R'};
    int count = 0;
    for(int i = 0; i < input.length(); i++) {
      if(input.charAt(i) != chars[i%3]) {
        count+=1;
      }
    }
    System.out.println(count);
  }
  public static void main(String[] args) {
    Conundrum thisInstance = new Conundrum();
    thisInstance.handleInput();
  }
}
