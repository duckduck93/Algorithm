function solution(sides) {
    const [min, max] = sides.sort((a, b) => a - b);
    const available = [...Array(max + min).keys()]
        .filter(arg => arg !== 0)
        .filter(arg => arg + min > max || arg > max);
    return available.length;
}

console.log(solution([1, 2]))
console.log(solution([3, 6]))
console.log(solution([11, 7]))