import axios from "axios";

const axiosClient = axios.create({
  baseURL: 'http://localhost:8000/api/',//process.env.REACT_APP_API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Optional: Add interceptors if needed (e.g., for adding auth tokens)
axiosClient.interceptors.request.use(
  (config) => {
    // You can add authorization tokens or other config here if needed
    return config;
  },
  (error) => Promise.reject(error)
);

export default axiosClient