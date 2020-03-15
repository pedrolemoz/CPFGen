# include <stdio.h>
# include <stdlib.h>
# include <time.h>

void generateCPF(int buildCPF[]);
int digit(int buildCPF[], int index);
int verifySum(int sum);

int main()
{
	int buildCPF[11];
	srand(time(NULL));

	generateCPF(buildCPF);

	return 0;
}

void generateCPF(int buildCPF[])
{
	int index = 10;

	for (int i = 0; i < 9; i++)
	{
		buildCPF[i] = rand() % 10;
	}

	for (int i = 9; i < 11; i++)
	{
		buildCPF[i] = digit(buildCPF, index);
		index++;
	}

	for (int i = 0; i < 11; i++)
	{
		printf("%d", buildCPF[i]);
	}
}

int digit(int buildCPF[], int index)
{
	int sum = 0, length = index - 1;

	for (int i = 0; i < length; i++)
	{
		sum += buildCPF[i] * index;
		index--;
	}

	return verifySum(sum);
}

int verifySum(int sum)
{
	if ((sum % 11) < 2)
		return 0;
	return 11 - (sum % 11);
}