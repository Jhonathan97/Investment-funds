import { useState, useEffect } from 'react';
import { getFund, subscribeFund, cancelFund, getHistory } from '../services/api';


export default function FundsList() {
    const [funds, setFunds] = useState([]);
    const [preference, setPreference] = useState("email");

    useEffect(() => {
        const fetchFunds = async () => {
            try {
                const response = await getFund();
                setFunds(response);
            } catch (error) {
                console.error('Error fetching funds:', error);
            }
        };

        fetchFunds();
    }, []);

    async function handleSubscribe(fundId) {
        try {
            const response = await subscribeFund(fundId, preference);
            console.log('Fund subscribed:', response);
        } catch (error) {
            console.error('Error subscribing to fund:', error);
        }
    }

    async function handleCancel(fundId) {
        try {
            const response = await cancelFund(fundId);
            console.log('Fund cancelled:', response);
        } catch (error) {
            console.error('Error cancelling fund:', error);
        }
    }

    return (
        <div className="bg-white shadow p-6 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Fondos disponibles</h2>
            <div className="mb-4">
                <label className="block mb-2 text-sm">Notificar por:</label>
                <select value={preference} onChange={(e) => setPreference(e.target.value)}>
                    <option value="email">Email</option>
                    <option value="sms">SMS</option>
                    <option value="both">Ambos</option>
                </select>
            </div>
            <ul className="space-y-4">
                {funds.map((fund) => (
                    <li key={fund.id} className="flex justify-between items-center">
                        <span className="font-bold">{fund.name}</span>
                        <span className="text-sm text-gray-500"> - Minimo: {fund.min_amount}</span>
                        <span className="text-sm text-gray-500"> - Categoria: {fund.category}</span>
                        <button onClick={() => handleSubscribe(fund.id)}
                            className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded">
                            Suscribirse</button>
                        <button onClick={() => handleCancel(fund.id)} 
                        className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded">
                        Cancelar</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}


