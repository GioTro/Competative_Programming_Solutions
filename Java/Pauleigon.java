import java.util.Scanner;

public class Pauleigon {

  public void handleInput() {
    Scanner io = new Scanner(System.in);
    int serves = io.nextInt();
    int games = io.nextInt() + io.nextInt();
    io.close();
    handleOutput(games, serves);
  }
  private void handleOutput(int games, int serves) {
    int toReturn = (games / serves);
    if(toReturn%2 == 0){
      System.out.println("paul");
    } else {
      System.out.println("opponent");
    }
  }
  public static void main(String[] args) {
    Pauleigon thisInstance = new Pauleigon();
    thisInstance.handleInput();
  }
}
