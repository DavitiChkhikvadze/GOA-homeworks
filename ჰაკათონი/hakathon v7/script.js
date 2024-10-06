// // 1 homework

// function joinArr(arr){
//     for(let i = 0;i < arr.length;i++){
//         return " ".join(arr[i]); 
//     }
// }

// console.log(joinArr([123,"sdfasd",645,"dsad"]))


// // 2 homework

// function maxMinNum(arr){
//     return Math.max(...arr) - Math.min(...arr)
// }

// console.log(maxMinNum([1,2,3,4,5,6]))


// // 4 homework

// function highestNum(arr){
//     return (Math.max(...arr))
// }

// console.log(highestNum([1,2,3,4,5,6,7,8,9,10]))


// // 5 homework

// function reverseString(string){
//     return string.split("").reverse().join("");
// }

// console.log(reverseString("gamarjoba"))



// factorial

function factorial(num){
    for(let i = num;i > 1;i--){
        return num * i
    }
}

console.log(factorial(5))