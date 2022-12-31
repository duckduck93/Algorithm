/**
 * @param {string} s
 */
function solution(s) {
    const mapper = {};
    return s.split('').map((value, index) => {
        if (!mapper.hasOwnProperty(value)) {
            mapper[value] = index;
            return -1;
        }
        const result = index - mapper[value];
        mapper[value] = index;
        return result;
    });
}

console.log(solution('banana'))