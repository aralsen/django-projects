import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [coins, setCoins] = useState([]);

    useEffect(() => {
        const coinsListUrl = 'http://localhost:8000/coins/';
        axios.get(coinsListUrl)
            .then(response => setCoins(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {coins.map((coin, index) => (
                    <div className="bg-white rounded-lg shadow-md overflow-hidden" key={index}>
                        <img
                            src={coin.photo_url}
                            alt={`${coin.name} logo`}
                            className="w-full h-48 object-cover"
                        />
                        <div className="p-4">
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">{coin.name}</h3>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}

export default App;
