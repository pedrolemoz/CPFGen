fun main() {
    var generator = GeneratorAlgorithm()
    
    for (i in 0..100){
        println(generator.generateCPF())
    }
}

class GeneratorAlgorithm() {
    fun generateCPF() : String {
        var buildCPF = ArrayList<Int>()
        
        for (i in 0..8) {
            buildCPF.add((0..9).random())
        }
        
        for (i in 0..1) {
            buildCPF.add(digit(buildCPF))
        }
  
        return buildString(buildCPF)
    }
    
    private fun digit(buildCPF : ArrayList<Int>) : Int {
        var sum: Int = 0
        var index: Int = buildCPF.size + 1
        
        for (i in buildCPF) {
            sum += i * index
            index--
        }
        
        return verifySum(sum)
    }
    
    private fun verifySum(sum: Int) : Int {
        if ((sum % 11) < 2) return 0 else return 11 - (sum % 11)
    }
    
    private fun buildString(buildCPF : ArrayList<Int>) : String {
        var getNumbers = ArrayList<String>()
        
        for (i in buildCPF) {
            getNumbers.add(i.toString())
        }
        
        var CPF: String = ""
        
        getNumbers.add(3, ".")
        getNumbers.add(7, ".")
        getNumbers.add(11, "-")
        
        for (i in getNumbers) {
            CPF += i.toString()
        }
        
        return CPF
    }
}
