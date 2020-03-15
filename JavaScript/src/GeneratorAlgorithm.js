function randomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

class GeneratorAlgorithm {
  generateCPF() {
    this.buildCPF = [];

    for (let i = 0; i < 9; i++) {
      this.buildCPF.push(randomInt(0, 9));
    }

    for (let i = 0; i < 2; i++) {
      this.buildCPF.push(this.digit());
    }

    return this.buildString();
  }

  digit() {
    let sum = 0;
    let index = this.buildCPF.length + 1;

    for (let i = 0; i < this.buildCPF.length; i++) {
      sum += this.buildCPF[i] * index;
      index--;
    }

    return this.verifySum(sum);
  }

  verifySum(sum) {
    if (sum % 11 < 2) {
      return 0;
    }
    return 11 - (sum % 11);
  }

  buildString() {
    let CPF = "";

    this.buildCPF.splice(3, 0, ".");
    this.buildCPF.splice(7, 0, ".");
    this.buildCPF.splice(11, 0, "-");

    for (let i = 0; i < this.buildCPF.length; i++) {
      CPF += this.buildCPF[i];
    }

    return CPF;
  }
}
