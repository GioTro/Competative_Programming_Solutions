import java.util.Scanner;

public class Hissing {

  public void handleInput() {
    Scanner io = new Scanner(System.in);
    String string = io.nextLine();
    io.close();
    handleOutput(string);
  }
  private void handleOutput(String string) {
    for(int i = 0; i < string.length() - 1; i++) {
      if(string.charAt(i) == 's' && string.charAt(i+1) == 's'){
        System.out.println("hiss");
        return;
      }
    }
    System.out.println("no hiss");
  }
  public static void main(String[] args) {
    Hissing thisInstance = new Hissing();
    thisInstance.handleInput();
  }
}
