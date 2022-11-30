function solution(routes) {
    routes.sort((o1, o2) => o1[1] - o2[1]);
    let camera = -30001;
    let cameras = [];
    for (const route of routes) {
        console.log(route)
        const [sta, end] = route;
        if (camera < sta) {
            cameras.push(end);
            camera = end;
        }
    }
    return cameras.length;
}

console.log(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]));
