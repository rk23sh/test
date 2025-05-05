import java.util.*;
import java.util.stream.*;
import java.math.*;
import java.io.*;

public class Menu {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int vertices, edges;
        vertices = scan.nextInt();
        edges = scan.nextInt();
        System.out.println(vertices + " " + edges);
        scan.close();

    }
}
