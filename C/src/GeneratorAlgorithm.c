# include <stdio.h>
# include <stdlib.h>
# include <time.h>

void generateCPF(int buildCPF[]);
int digit(int buildCPF[], int index);
int verifySum(int sum);
void buildString(int buildCPF[]);

int main() {
  int buildCPF[11];
  srand(time(NULL));

  generateCPF(buildCPF);

  return 0;
}

void generateCPF(int buildCPF[]) {
  int index = 10;

  for (int i = 0; i < 9; i++) {
    buildCPF[i] = rand() % 10;
  }

  for (int i = 9; i < 11; i++) {
    buildCPF[i] = digit(buildCPF, index);
    index++;
  }

  buildString(buildCPF);
}

int digit(int buildCPF[], int index) {
  int sum = 0, length = index - 1;

  for (int i = 0; i < length; i++) {
    sum += buildCPF[i] * index;
    index--;
  }

  return verifySum(sum);
}

int verifySum(int sum) {
  if ((sum % 11) < 2)
    return 0;
  return 11 - (sum % 11);
}

void buildString(int buildCPF[]) {
  char cpf[14];

  for (int i = 0; i < 11; i++) {
    cpf[i] = buildCPF[i] + '0';
  }

  for (int i = 13; i >= 3; i--) {
    cpf[i + 1] = cpf[i];
  }

  for (int i = 13; i >= 7; i--) {
    cpf[i + 1] = cpf[i];
  }

  for (int i = 13; i >= 11; i--) {
    cpf[i + 1] = cpf[i];
  }

  cpf[3] = '.';
  cpf[7] = '.';
  cpf[11] = '-';

  printf("%s", cpf);
}
