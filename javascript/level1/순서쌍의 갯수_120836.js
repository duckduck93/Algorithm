function solution(n) {
    const l = [];
    for (let i = 0; i <= n; i++) {
        if (n % i === 0) l.push(i);
    }
    return l.length;
}

console.log(solution(20));
console.log(solution(100));