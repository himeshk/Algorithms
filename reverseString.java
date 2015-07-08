import java.util.Arrays;
import java.util.*;

public class reverseString {
	public static void main(String [] args) {
		HashSet<Character> test = new HashSet<Character>();
		char [] arr = args[0].toCharArray();
		for (int loop1 = 0 ; loop1 < arr.length ; loop1++) {
			test.add(arr[loop1]);
		}
		System.out.println(test);
		
		
		/*int charPosition[] = new int[255];
		for (int loop1 = 0; loop1 < arr.length ;loop1++) {
			if (charPosition[(int) arr[loop1]] > 0) {
				continue;
			}
			charPosition[(int) arr[loop1]] = loop1;
		}*/
		//Arrays.sort(charPosition);
		
	}
}