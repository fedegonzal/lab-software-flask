const ws = new WebSocket(`ws://127.0.0.1:5000/ws`);

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const action = data.action;
    const university = data.data;
    console.log(action);
    console.log(university);
    updateTable();
}

ws.onopen = () => {
    console.log('Connected');
}

ws.onclose = () => {
    console.log('Disconnected');
}
