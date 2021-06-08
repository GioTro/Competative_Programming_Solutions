import java.util.Arrays;
import java.util.Scanner;

/**
 * Not so stylish solution for kattis problem: https://open.kattis.com/problems/abc
 */

public class ABC {
    int[] num;

    private void execute(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == 'A') {
                sb.append(num[0]+" ");
            }
            if (s.charAt(i) == 'B') {
                sb.append(num[1]+" ");
            }
            if (s.charAt(i) == 'C') {
                sb.append(num[2]+" ");
            }
        }
        sb.trimToSize();
        System.out.println(sb.toString());
    }
    private void convertMeToInt(String[] s) {
        num = new int[s.length];
        int j = 0;
        for (String i : s) {
            num[j++] = Integer.parseInt(i);
        }
        // The logic of execute method needs a sorted array
        Arrays.sort(num);
    }


    public void input() {
        Scanner io = new Scanner(System.in);
        String s = io.nextLine();
        String[] parts = s.split("\\s");
        convertMeToInt(parts);

        s = io.nextLine();
        io.close();
        execute(s);
    }

    public static void main(String[] args) {
        ABC thisInstance = new ABC();
        thisInstance.input();
    }
}
