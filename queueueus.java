import java.util.*;
class queueueus {
	static LinkedList<Integer> ll;
	static long counter;
	public static void main(String [] args) {
		ll = new LinkedList<Integer>();
	}
	public static void push(int i) {
		ll.add(i);
		counter++;	
		
	}
	public static int get() {
		if (counter > 0) 
			return -1;
		return ll.getFirst();
		
	}
	public static int pop() {
		if (counter == 0) {
			return -1;
		}
		int i = ll.pollFirst();
		counter--;
		return i;
	}

}