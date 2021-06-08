/**
Solution to kattis problem source: https://open.kattis.com/problems/quadrant
*/

import java.util.Scanner;
public class Quadrant {

  int x, y;
  int quad;

  public void quadEval(){
    if (x > 0) {
      if (y > 0) {
        quad = 1;
      } else {
        quad = 4;
      }
    } else {
      if (y > 0) {
        quad = 2;
      } else {
        quad = 3;
      }
    }
  }
  public void handleInput() {
  Scanner kattio = new Scanner(System.in);
  x = kattio.nextInt();
  y = kattio.nextInt();
  kattio.close();
  }
  public void handleOutput() {
    System.out.println(quad);
  }

  public static void main(String[] args) {
    Quadrant thisInstance = new Quadrant();
    thisInstance.handleInput();
    thisInstance.quadEval();
    thisInstance.handleOutput();
  }
}
