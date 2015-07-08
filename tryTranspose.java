import java.util.*;

public class tryTranspose {
	public static void main(String args[]) {
		Scanner scr = new Scanner(System.in);
		int length1 = scr.nextInt();
		int arr9[][] = new int[length1][length1];
		for (int loop1 = 0 ; loop1 < length1 ; loop1++) {
			for(int loop2 = 0 ; loop2 < length1 ; loop2++) {
				arr9[loop1][loop2] = scr.nextInt();
			}
		}
		printArr(arr9);
		for(int loop1 = 0 ; loop1 < length1 ; loop1++) {
			for (int loop2 = loop1 ; loop2 < (length1 - 1) ; loop2++) {
				int temp = arr9[loop1][loop2+1];
				arr9[loop1][loop2 + 1] = arr9[loop2 + 1][loop1];
				arr9[loop2 + 1][loop1] = temp;	
			}
			
		}
		printArr(arr9);
	}
	public static void printArr(int arr9[][]) {
				for (int loop1 = 0 ; loop1 < arr9.length ; loop1++) {
			for(int loop2 = 0 ; loop2 < arr9.length ; loop2++) {
				System.out.print(arr9[loop1][loop2] + " " );
			}
			System.out.println();
		}
			

	}
}