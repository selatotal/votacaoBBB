public class Collatz {

	public static void main(String[] args) {
		long maior = 1;
		long numSeqMaior = 0;

		for (long n = 1; n < 1000000; n++) {
			long val = n;
			long numseq=1;
			while (val > 1) {
				if (val % 2 == 0) {
					val /= 2;
				} else {
					val = 3 * val + 1;
				}
				numseq++;
			}
			if (numseq > numSeqMaior) {
				maior = n;
				numSeqMaior = numseq;
			}
		}
		System.out.println(maior + " " + numSeqMaior);
	}

}
