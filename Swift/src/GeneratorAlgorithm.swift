import Foundation

class GeneratorAlgorithm {
    func generateCPF() -> String {
        var buildCPF = [Int]()
        
        for _ in 0...8 {
            buildCPF.append(Int.random(in: 0...9))
        }
        
        for _ in 0...1 {
            buildCPF.append(digit(buildCPF))
        }
  
        return buildString(buildCPF)
    }
    
    func digit(_ buildCPF : [Int]) -> Int {
        var sum: Int = 0
        var index: Int = buildCPF.count + 1
        
        for i in buildCPF {
            sum += i * index
            index -= 1
        }
        
        return verifySum(sum)
    }
    
    func verifySum(_ sum: Int) -> Int {
        if (sum % 11) < 2 {
            return 0
        }
        
        return 11 - (sum % 11)
    }
    
    func buildString(_ buildCPF : [Int]) -> String {
        var getNumbers = [String]()
        
        for i in buildCPF {
            getNumbers.append(String(i))
        }
        
        var CPF: String = ""
        
        getNumbers.insert(".", at: 3)
        getNumbers.insert(".", at: 7)
        getNumbers.insert("-", at: 11)
        
        for i in getNumbers {
            CPF += String(i)
        }
        
        return CPF
    }
}


var generator = GeneratorAlgorithm()

for _ in 0...100 {
    print(generator.generateCPF())
}
