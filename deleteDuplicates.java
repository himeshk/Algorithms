import java.util.*;
public class deleteDuplicates {
	public static void main(String args[]) {
		LinkedList<Integer> ll = new LinkedList();
		HashSet<Integer> hm = new HashSet();
		Scanner scr = new Scanner(System.in);
		int loop1 = scr.nextInt();
		for (int loop2 = 0 ; loop2 < loop1 ; loop2++) {
			ll.add(scr.nextInt());
		}
		try {
			findDuplicate(ll , hm);
		}
		catch(Exception e) {
			
		}
		
	}
	public static void findDuplicate(LinkedList ll , HashSet hm) throws Exception {
		//ListIterator li = ll.listIterator();	
		int loop1 = 0 ; 
		while(true){
			hm.add(ll.get(loop1));
			//ll.remove(loop1);
			loop1++;
		}
		//ll = new LinkedList(hm);
	}

}