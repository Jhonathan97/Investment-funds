import { useState, useEffect } from 'react';
import { getHistory } from '../services/api';


export default function HistoryList() {
    const [history, setHistory] = useState([]);

    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const response = await getHistory();
                setHistory(response);
            } catch (error) {
                console.error('Error fetching history:', error);
            }
        };

        fetchHistory();
    }, []);

    return (
        <div>
            <h2>Historial de transacciones</h2>
            <ul>
                {history.map((transaction) => (
                    <li key={transaction.id}>
                        <span>{transaction.type} en  {transaction.fund_name}</span>
                        <span>Por un valor de {transaction.amount}</span>
                        <span>Fecha: {new Date(transaction.date).toLocaleDateString()}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
}
