import java.util.*;
class queuesUsingStack {
	static int arr1[];
	static int arr2[];
	static int counter;
	static int counter1;
	public static void main(String [] args) {
		counter = 21 ; 
		counter1 = 21;
		arr1  = new int[counter+1];
		arr2  = new int[counter+1];

		Scanner scr = new Scanner(System.in);	
		int temp ;
		while ((temp = scr.nextInt()) > 0) {
			 {
				int temp1;
				System.out.println(" In 1st loop1 " );
				while((temp1 = removeFromQueue()) > -1) {
					addToQueue1(temp1);
					System.out.print( temp1 + " " );
				}
				System.out.println("");
				System.out.println(addToQueue(temp));
				System.out.println("in second loop1 ");
				while((temp1 = removeFromQueue1()) > -1) {
					addToQueue(temp1);	
					System.out.print(" " + temp1);
				}				
				System.out.println("");
			}
		}
		while ((temp = removeFromQueue()) > 0) {
			 {
				System.out.println(temp);
			}
		}
		

	}
	public static boolean addToQueue(int temp) {
		if (counter == 0) {
			return false;
		}
		else {
			arr1[--counter] = temp;
			//counter--;
			return true;
		}
	}
	public static boolean addToQueue1(int temp) {
		if (counter1 == 0) {
			return false;
		}
		else {
			arr2[--counter1] = temp;
			//counter--;
			return true;
		}
	}

	public static int removeFromQueue() {
		if (counter > 20) {
			return -1;
		}
		else {
			return arr1[counter++];
			
		}
		
	}
	public static int removeFromQueue1() {
		if (counter1 > 20) {
			return -1;
		}
		else {
			return arr2[counter1++];
			
		}
		
	}

}