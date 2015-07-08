import java.util.*;
class stacks {
	static LinkedList<Integer> ll;
	static long counter;
	
	public static void main(String []args) {
		ll = new LinkedList<Integer>();
		push(10);
		System.out.println("" + pop());
		System.out.println("" + pop());

	
	}
	public static void push(int i) {
		ll.add(i);
		counter++;	
		
	}
	public static int get() {
		if (counter > 0) 
			return -1;
		return ll.getLast();
		
	}
	public static int pop() {
		if (counter == 0) {
			return -1;
		}
		int i = ll.pollLast();
		counter--;
		return i;
	}

}