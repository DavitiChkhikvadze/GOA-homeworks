function descriminantSolution(a,b,c){
    let descriminant = 0
    let solution1 = 0
    let solution2 = 0

    if (b % 2 !== 0){
        descriminant += b**2 - 4*a*c
        solution1 += (-1*b - Math.sqrt(descriminant)) / (2*a)
        solution2 += (-1*b + Math.sqrt(descriminant)) / (2*a)
    } else {
        descriminant += (b/2)**2 - a*c
        solution1 += (-1*b/2 - Math.sqrt(descriminant)) / a
        solution2 += (-1*b/2 + Math.sqrt(descriminant)) / a
    }
    
    return solution1, solution2
}

console.log(descriminantSolution(1, -1, -6))