/**
*Solution for Kattis problem source: https://open.kattis.com/problems/trik
*/
import java.util.Scanner;

public class Trik {
  private String moves;
  private int[] board = { 1, 0, 0 };
  private char a = 'A';
  private char b = 'B';
  private char c = 'C';

  public void playGame(){
    for (int turns = 0; turns < moves.length(); turns++) {
      if (a == moves.charAt(turns)){
        int hold = board[0];
        board[0] = board[1];
        board[1] = hold;
      }
      if (b == moves.charAt(turns)){
        int hold = board[1];
        board[1] = board[2];
        board[2] = hold;
      }
      if (c == moves.charAt(turns)){
        int hold = board[2];
        board[2] = board[0];
        board[0] = hold;
      }
    }
  }

  public void handleInput() {
    Scanner kattio = new Scanner(System.in);
    moves = kattio.next();
    kattio.close();
  }
  public void handleOutput(){
    for (int index = 0; index < board.length; index++){
      if (board[index] == 1){
        int toPrint = index + 1;
        System.out.println(toPrint);
      }
    }
  }
  public static void main(String[] args) {
    Trik thisInstance = new Trik();
    thisInstance.handleInput();
    thisInstance.playGame();
    thisInstance.handleOutput();
  }
}
