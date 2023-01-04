/**
 * @param {string} num
 * @return {number}
 */
function binaryToDecimal(num) {
    return num.split('')
        .reverse()
        .map((value, index) => value * Math.pow(2, index))
        .reduce((pre, cur) => pre + cur, 0);
}

/**
 * @param {number} num
 * @return {string}
 */
function decimalToBinary(num) {
    const result = [];
    while (num) {
        result.push(num % 2);
        num = Math.floor(num / 2);
    }
    if (result.length === 0) return '0';
    return result.reverse().join('')
}

function solution(bin1, bin2) {
    const dec1 = binaryToDecimal(bin1);
    const dec2 = binaryToDecimal(bin2);
    console.log(dec1, bin1);
    console.log(dec2, bin2);
    return decimalToBinary(dec1 + dec2);
}

console.log(solution("10", "11"));
console.log(solution("1001", "1111"));
console.log(solution("0", "0"));
console.log(solution("1", "1"));
