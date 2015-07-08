import java.util.*;
import static java.lang.System.out;
class sortStack {
	public static void main(String [] args) {
		Stack<Integer> stcSort = new Stack();
		Stack<Integer> stcTemp = new Stack();
		Scanner scr = new Scanner(System.in);
		int temp;
		int counter = -1;
		while ((temp = scr.nextInt()) > 0) {
			stcSort.push(temp);
			counter++;
		}
		int current = 0;
		//out.println(counter);
		for (int loop1 = 0; loop1 <= counter ; loop1++) {
			current = -1;
			
			for (int loop2 = 0; loop2 <= (counter-loop1);loop2++) {
				//System.out.println("in here ");
				temp = stcSort.pop();
				//System.out.print
				out.println("" + temp); 
				if (temp > current) {
					if (current  > 0) {
						stcTemp.push(current);
						System.out.println("pushed here ");
					}
					current = temp;
				}
				else {
					stcTemp.push(temp);
					System.out.println("pushed here 1");
				}
			}
			stcSort.push(current);
			for (int loop2 = 0; loop2 <= (counter-loop1-1);loop2++) {
				System.out.println(loop2);
				temp = stcTemp.pop();
				stcSort.push(temp);
			}
		}
		for (int loop1 = 0; loop1 <= counter ; loop1++) {
			System.out.println(stcSort.pop());
		}

	}
}