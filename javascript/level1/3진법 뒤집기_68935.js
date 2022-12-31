/**
 * @param {number} n
 * @return {number[]}
 */
function toTernary(n) {
    const answer = []
    while (n) {
        answer.push(n % 3);
        n = Math.floor(n / 3);
    }
    return answer.reverse();
}

/**
 * @param {number[]} n
 * @return number
 */
function toDecimal(n) {
    return n.reverse()
        .reduce((pre, cur, currentIndex) => {
            const target = cur * Math.pow(3, currentIndex);
            return pre + target
        }, 0);
}

/**
 * @param {number} n
 */
function solution(n) {
    const ternary = toTernary(n);
    const reverse = ternary.reverse();
    return toDecimal(reverse);
}


console.log(solution(45))
console.log(solution(125))