/**
 * @param {number[][]} data
 * @param {number} col
 * @param {number} row_begin
 * @param {number} row_end
 */
function solution(data, col, row_begin, row_end) {
    data = data.sort((row1, row2) => {
        if (row1[col - 1] !== row2[col - 1]) return row1[col - 1] - row2[col - 1]; // 오름차순
        return row2[0] - row1[0]; // 내림차순
    });

    let answer = 0;
    for (let i = row_begin; i <= row_end; i++) {
        const S = data[i - 1].map(arg => arg % i).reduce((pre, cur) => pre + cur, 0);
        answer = answer ^ S;
    }
    return answer;
}

console.log(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))