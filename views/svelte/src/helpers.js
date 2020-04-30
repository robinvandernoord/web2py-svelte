// simplify some common things

export function apiroute(endpoint) {
    return route('api', endpoint + '.json');
}

export function route(controller, method) {
    /**
     * @var appname: appname from window (from backend)
     */
    if(!method) {
        method = controller;
        controller = 'default';
    }
    return `/${appname}/${controller}/${method}`;
}

export async function apirequest(endpoint) {
    // example helper to do a GET request to api/endpoint
    const result = await fetch(apiroute(endpoint));
    if(result.status === 200) {
        return await result.json();
    } else {
        throw await result.text();
    }
}
