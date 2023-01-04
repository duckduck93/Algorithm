/**
 * @param {string} arg
 * @return {Map<string, number>}
 */
function makeCounter(arg) {
    return arg.split('').reduce((counter, value) => {
        if (!counter.has(value)) {
            counter.set(value, 0);
        }
        counter.set(value, counter.get(value) + 1);
        return counter;
    }, new Map());
}

/**
 * @param {Map<string, number>} counter1
 * @param {Map<string, number>} counter2
 * @return {string}
 */
function find(counter1, counter2) {
    const result = [];
    for (const i of [...new Array(10).keys()].reverse()) {
        const index = i.toString();
        const count = Math.min(counter1.get(index), counter2.get(index)) ?? 0;
        if (count !== 0) result.push(index.repeat(count));
    }
    const answer = result.join('').toString();
    const int = parseInt(answer);
    if (isNaN(int)) return '-1';
    if (!int) return '0';
    return answer;
}

/**
 * @param {string} X
 * @param {string} Y
 * @return string
 */
function solution(X, Y) {
    const counter1 = makeCounter(X);
    const counter2 = makeCounter(Y);
    return find(counter1, counter2);
}

console.log(solution("100", "2345"), "-1");
console.log(solution("100", "203045"), "0");
console.log(solution("100", "123450"), "10");
console.log(solution("12321", "42531"), "321");
console.log(solution("5525", "1255"), "552");
console.log(solution("0".repeat(3_000_000), "0".repeat(3_000_000)), '0');
// console.log(solution("9".repeat(3_000_000), "9".repeat(3_000_000)), "552");
