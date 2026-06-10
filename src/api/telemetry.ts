import axios from 'axios';
import { PlantData } from '../types';

const API_BASE_URL = 'https://api.nexora-plantation.ai/v1';

export const fetchTelemetry = async (stationId: string): Promise<PlantData> => {
  const response = await axios.get(`${API_BASE_URL}/telemetry/${stationId}`);
  return response.data;
};

export const updateIrrigation = async (stationId: string, volume: number) => {
  return axios.post(`${API_BASE_URL}/irrigation/adjust`, { stationId, volume });
};
