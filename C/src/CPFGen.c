# include <stdio.h>

void generate(int buildCPF[]){
	int i, index = 10;
	
	for (i = 0; i < 9; i++){
		buildCPF[i] = rand() % 10;
	}
	
	for (i = 9; i < 11; i++){
		buildCPF[i] = digit(buildCPF, index);
		index++;
	}
	
	for (i = 0; i < 11; i++){
		printf("%d", buildCPF[i]);
	}
}

int digit(int buildCPF[], int index){
	int i, sum = 0, length = index - 1;
	
	for (i = 0; i < length; i++){
		sum += buildCPF[i] * index;
		index--;
	}
	
	return verifySum(sum);
}

int verifySum(int sum){
	if ((sum % 11) < 2)
		return 0;
	else
		return 11 - (sum % 11);
}

int main(){
	int buildCPF[11];
	srand(time(NULL));
	
	generate(buildCPF);
	
	return 0;
}
