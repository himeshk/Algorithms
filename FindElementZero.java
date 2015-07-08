import java.util.*;
class FindElementZero {
	public static void main(String args[]) {
		Scanner scr = new Scanner(System.in);
		int matX = scr.nextInt();
		int matY = scr.nextInt();
		int mat[][] = new int[matX][matY];
		int ifZero[] = new int[matY];
		for(int loop2 = 0 ; loop2 < matY ; loop2++) {
			ifZero[loop2] = -1;
		}
		for (int loop1 = 0 ; loop1 < matX ; loop1++) {
			for (int loop2 = 0 ; loop2 < matY ; loop2++) {
				mat[loop1][loop2] = scr.nextInt();
				if (mat[loop1][loop2] == 0) {
					ifZero[loop2] = loop1;
				}
			}
		}
		printArr(mat , matY , matX);
		for (int loop2 = 0 ; loop2 < matY ; loop2++) {
			if (ifZero[loop2] > -1) {
				for (int loop1 = 0 ; loop1 < matX;loop1++) {
					mat[loop1][loop2] = 0;
				}
				for (int loop1 = 0 ; loop1 < matY;loop1++) {
					mat[ifZero[loop2]][loop1] = 0;
				}
			}
			
		}
		printArr(mat , matY , matX);
	}
	public static void printArr(int arr[][] ,int col , int row){
			for (int loop1 = 0 ; loop1 < row ; loop1++) {
				for (int loop2 = 0 ; loop2 < col ; loop2++) {
					System.out.print(arr[loop1][loop2] + "  " );
				}
				System.out.println();
			}
	}
}