import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const fetchStocks = async () => {
    try {
        const response = await axios.get(`${API_URL}/optimusstocks/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching stocks:', error);
        throw error;
    }
};