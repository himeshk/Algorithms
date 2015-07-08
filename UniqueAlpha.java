class UniqueAlpha {
	public static void main(String args[]) {
		if (args[0] == null) {
			System.exit(0);
		}
		char temp[] = args[0].toCharArray();
		boolean bl[] = new boolean[255];
		for (int loop1 = 0 ; loop1 < 255; loop1++) {
			bl[loop1] = false;
		}
		for (char ch : temp) {
			if (bl[(int)ch] == true) {
				System.out.println(" Character repeat !" );
				break;
			}
			bl[(int)ch] = true;
		}
	}
	
}