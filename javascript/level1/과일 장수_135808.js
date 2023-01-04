function solution(k, m, score) {
    score = score.sort().reverse();

    const items = [];
    let counter = [];
    for (const s of score) {
        counter.push(s);
        if (counter.length === m) {
            items.push(counter);
            counter = [];
        }
    }

    let answer = 0;
    for (const item of items) {
        const min = Math.min(...item);
        answer += (min * m);
    }

    return answer;
}

console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]));
console.log(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]));