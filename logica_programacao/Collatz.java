public class Collatz {

	public static void main(String[] args) {
		int maior = 1;
		int numSeqMaior = 0;
		
		for (int n = 1; n < 1000000; n++) {
			int val = n;
			int numseq=0;
			while (val > 1) {
				if (val % 2 == 0) {
					val /= 2;
				} else {
					val = 3 * val + 1;
				}
				numseq++;
			}
			if (numseq > maior) {
				maior = n;
				numSeqMaior = numseq;
			}
		}
		System.out.println(maior + " " + numSeqMaior);
	}

}
