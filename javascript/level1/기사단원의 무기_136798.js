/**
 * @param {number} number
 */
function findDivisor(number) {
    let result = 0;
    for (let i = 1; i * i <= number; i++) {
        if (i * i === number) result += 1;
        else if (number % i === 0) result += 2;
    }
    return result;
}

/**
 * @param {number} number
 * @param {number} limit
 * @param {number} power
 */
function solution(number, limit, power) {
    return [...Array(number).keys()]
        .map(arg => arg + 1)
        .map(arg => findDivisor(arg))
        .map(arg => arg > limit ? power : arg)
        .reduce((pre, cur) => pre + cur, 0);
}

console.log(solution(5, 3, 2));
console.log(solution(10, 3, 2));
