import java.util.*;
class IsSubstring {
	public static void main(String [] args) {
		String str1 = args[0];
		String str2 = args[1];
		System.out.println(koiCheckKaroBhai(str1 , str2));
	}
	public static boolean koiCheckKaroBhai(String str1 , String str2) {
		String str3 = str1 + str1;
		if(str1 == null || str2 == null)	return false;
		if((str3.indexOf(str2)) > 0)	return true;
		else return false;
			
	}	

}