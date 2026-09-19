import {useState, useEffect} from "react";

function Receiver() {
    const [message, setMessage] = useState(null);

    useEffect(() => {
        async function fetchMessage() {
            const response = await fetch("http://127.0.0.1:8000/greetings");

            const data = await response.json();
            setMessage(data.message);
        }

        fetchMessage();
    }, []);

    return <p>{message}</p>;
}
export default Receiver;