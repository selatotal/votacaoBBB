
public class SubCadeia {

	public static void main(String[] args) {
		// Array com o conjunto informado
		int[] conjunto = { 2, -4, 6, 8, -10, 100, -6, 5 };
		int tamConjunto = conjunto.length;
		int maiorSoma=0;
		int maiorI=0, maiorJ=0;
		int i, j=0;
		
		for (i=0; i < tamConjunto; i++){
			for (j=i+1; j < tamConjunto; j++){
				int soma = 0;
				for (int k=i; k <= j; k++){
					soma+=conjunto[k];
				}
				if (soma > maiorSoma){
					maiorI=i;
					maiorJ=j;
					maiorSoma = soma;
				}
			}
		}
		
		System.out.println("[" + maiorI + "," + maiorJ + "] Soma: " + maiorSoma);

	}

}
