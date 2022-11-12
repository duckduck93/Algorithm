function findRoom(roomMap, num) {
    if (!roomMap.has(num)) {
        roomMap.set(num, num + 1);
        return num;
    }
    const next = findRoom(roomMap, roomMap.get(num));
    roomMap.set(num, next + 1);
    return next;
}

function solution(k, room_number) {
    const answer = [];
    const roomMap = new Map();
    for (const room of room_number) {
        answer.push(findRoom(roomMap, room));
    }
    return answer;
}

console.log(solution(10, [1, 3, 4, 1, 3, 1]))