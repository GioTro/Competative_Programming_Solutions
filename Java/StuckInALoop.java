/**
Solution for kattis problem source: https://open.kattis.com/problems/timeloop
*/
import java.util.Scanner;

public class StuckInALoop {
  int loop;
  String abra = " Abracadabra";

  public void loop(){
    for (int i=1; i < (loop + 1); i++) {
      System.out.println(i + abra);
    }
  }
  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    loop = kattio.nextInt();
    kattio.close();
  }
  public static void main(String[] args) {
    StuckInALoop thisInstance = new StuckInALoop();
    thisInstance.handleInput();
    thisInstance.loop();
  }
}
