import axios from 'axios';

const API_URL = "https://eg0dt0v9kl.execute-api.us-east-1.amazonaws.com/prod";


// Obtener todos los fondos
export async function getFund() {
    const res = await axios.get(`${API_URL}/funds/`);
    return res.data;
}

// Suscribir a un fondo
export async function subscribeFund(fund_id, preference) {
    const res = await axios.post(`${API_URL}/funds/subscribe`, {
        fund_id,
        notification_preference: preference
    });
    return res.data;
}

// Cancelar suscripción de un fondo
export async function cancelFund(fund_id) {
    const res = await axios.post(`${API_URL}/funds/cancel`, {
        fund_id
    });
    return res.data;
}

// Obtener historial
export async function getHistory() {
    const res = await axios.get(`${API_URL}/history`);
    return res.data;
}
