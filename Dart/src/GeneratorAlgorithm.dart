import 'dart:math' show Random;

class GeneratorAlgorithm {
  String generateCPF() {
    Random random = Random();
    var buildCPF = [];

    for (var i = 0; i < 9; i++) {
      buildCPF.add(random.nextInt(9));
    }

    for (var i = 0; i < 2; i++) {
      buildCPF.add(digit(buildCPF));
    }

    return buildString(buildCPF);
  }

  int digit(List buildCPF) {
    var sum = 0;
    var index = buildCPF.length + 1;

    for (var i = 0; i < buildCPF.length; i++) {
      sum += buildCPF[i] * index;
      index -= 1;
    }

    return verifySum(sum);
  }

  int verifySum(int sum) {
    if ((sum % 11) < 2) {
      return 0;
    }
    return 11 - (sum % 11);
  }

  String buildString(List buildCPF) {
    var CPF = "";
    buildCPF.insert(3, ".");
    buildCPF.insert(7, ".");
    buildCPF.insert(11, "-");

    for (var i = 0; i < buildCPF.length; i++) {
      CPF += buildCPF[i].toString();
    }

    return CPF;
  }
}

void main() {
  GeneratorAlgorithm CPF = GeneratorAlgorithm();
  var generated = CPF.generateCPF();
  print(generated);
}
