import axios from "axios";

const API_URL = 'http://localhost:8000/api';

interface User {
    id: number;
    username: string;
    // Add other user fields here if necessary
}

export const fetchUsers = async (): Promise<User[]> => {
    try {
        const response = await axios.get<User[]>(`${API_URL}/users/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

export const fetchUser = async (id: number): Promise<User> => {
    try {
        const response = await axios.get<User>(`${API_URL}/users/${id}/`);
        return response.data;
    } catch (error) {
        console.error(`Error fetching user with id ${id}:`, error);
        throw error;
    }
};

export const createUser = async (user: User): Promise<User> => {
    try {
        const response = await axios.post<User>(`${API_URL}/users/`, user);
        return response.data;
    } catch (error) {
        console.error('Error creating user:', error);
        throw error;
    }
};

export const updateUser = async (id: number, user: User): Promise<User> => {
    try {
        const response = await axios.put<User>(`${API_URL}/users/${id}/`, user);
        return response.data;
    } catch (error) {
        console.error(`Error updating user with id ${id}:`, error);
        throw error;
    }
};

export const deleteUser = async (id: number): Promise<void> => {
    try {
        await axios.delete(`${API_URL}/users/${id}/`);
    } catch (error) {
        console.error(`Error deleting user with id ${id}:`, error);
        throw error;
    }
};
