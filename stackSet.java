import java.util.*;
class stackSet
{
	public static void main(String args[]) {
		int counter = 0;
		stackSets c = new stackSets();		
		ArrayList<stackSets> ss = new ArrayList<stackSets>();
		ss.add(c); 	
		Scanner scr = new Scanner(System.in);
		int temp = 0;
		while ((temp = scr.nextInt()) > 0) {
			
			boolean b = ss.get(ss.size() - 1).add(temp);
			System.out.println(b);
			if (b == false) {
				ss.add(new stackSets());
				ss.get(ss.size() - 1).add(temp);
			}			
		}
		while ((temp = scr.nextInt()) > 0) {
			
			boolean b = ss.get(ss.size() - 1).pop();
			System.out.println(b);
			if (b == false) {
				ss.remove(ss.get(ss.size() - 1));
				ss.get(ss.size() - 1).pop();
			}			
		}
		
	}
}

class stackSets {

	private int capacity;
	LinkedList<Integer> arr;
	int currentCounter;
	public stackSets (){
		capacity = 3;
		//arr = new int[capacity];
		arr = new LinkedList<Integer>();
		currentCounter = 0;
	}
	public boolean add(int num) {
		if (currentCounter == capacity) {
			
			return false;
		}
		else {
			arr.add(num);
			currentCounter++;
			return true;
		}
		
	}
	public boolean pop() {
		if ( currentCounter == 0) {
			return false;
		}
		int i = arr.pollLast();
		System.out.println(i);
		currentCounter--;
		return true;
	}
}