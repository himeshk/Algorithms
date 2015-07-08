import java.util.*;
class addLinkedList {
 public static void main(String args[]) {
	LinkedList<Integer> lst = new LinkedList<Integer>();
	LinkedList<Integer> lst2 = new LinkedList<Integer>();
	LinkedList<Integer> lst3 = new LinkedList<Integer>();
	lst.add(9);
	lst.add(9);
	lst.add(0);
	lst2.add(9);
	lst2.add(9);
	lst2.add(9);
	int longerLen = lst2.size();
	if (lst.size() > lst2.size()){
		longerLen = lst.size();
	} 
	ListIterator<Integer> li1 = lst.listIterator(0);
	ListIterator<Integer> li2 = lst2.listIterator(0);
	int element1 = 0 , element2 = 0 , carrier = 0;
	for (int loop1 = 0 ; loop1 < longerLen ; loop1++) {
		if(li1.hasNext()) {
			element1 = li1.next();
		}
		if(li2.hasNext()) {
			element2 = li2.next();
		}
		lst3.add((element1+element2+carrier)%10);
		carrier = ((element1 + element2 + carrier)/10);
		element1 = 0;
		element2 = 0;
		
		
		
	}
	if (carrier > 0) {
		lst3.add(carrier);
	}
	ListIterator<Integer> li3 = lst3.listIterator(0);
	for (int loop1 = 0 ; loop1 < lst3.size();loop1++) System.out.println(li3.next());
 }

}