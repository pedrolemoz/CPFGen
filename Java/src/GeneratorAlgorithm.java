import java.util.*;

public class GeneratorAlgorithm {
	public static void main(String[] args) {
		Generator CPF = new Generator();
		System.out.println(CPF.generateCPF());
	}
}

class Generator{
	private ArrayList<Integer> buildCPF = new ArrayList<Integer>();
	private String formattedCPF;
	Random random = new Random();
	
	public String generateCPF(){
		for (int i = 0; i < 9; i++){
			buildCPF.add(random.nextInt(10));
		}
		
		for (int i = 0; i < 2; i++){
			buildCPF.add(digit());
		}
		
		formattedCPF = buildString();
		
		return formattedCPF;
	}
	
	
	private int digit(){
		int sum = 0, index = buildCPF.size() + 1;
		
		for (int i = 0; i < buildCPF.size(); i++){
			sum += buildCPF.get(i) * index;
			index--;
		}
		
		return verifySum(sum);
	}
	
	private int verifySum(int sum){
		if ((sum % 11) < 2){
			return 0;
		}
		else{
			return 11 - (sum % 11);
		}
	}
	
	private String buildString(){
		ArrayList<String> getNumbers = new ArrayList<String>();
		StringBuilder formattedCPF = new StringBuilder();
		
		for (int i = 0; i < buildCPF.size(); i++){
			getNumbers.add(Integer.toString(buildCPF.get(i)));
		}
		
		getNumbers.add(3, ".");
		getNumbers.add(7, ".");
		getNumbers.add(11, "-");
		
		for (int i = 0; i < getNumbers.size(); i++){
			formattedCPF.append(getNumbers.get(i));
		}
		
		return formattedCPF.toString();
	}
}
