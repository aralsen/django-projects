import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import { motion } from 'framer-motion';

function App() {
    const [coins, setCoins] = useState([]);
    const [selectedCoin, setSelectedCoin] = useState(null);

    useEffect(() => {
        const coinsListUrl = 'http://localhost:8000/coins/';
        axios.get(coinsListUrl)
            .then(response => setCoins(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    const handleCoinClick = (coin) => {
        setSelectedCoin(coin);
    };

    const handleCoinClose = () => {
        setSelectedCoin(null);
    };

    return (
        <>
            <motion.div
                className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.5 }}
            >
                {coins.map((coin, index) => (
                    <motion.div
                        className="bg-white rounded-lg shadow-md overflow-hidden cursor-pointer"
                        key={index}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => handleCoinClick(coin)}
                    >
                        <motion.img
                            src={coin.photo_url}
                            alt={`${coin.name}`}
                            className="w-full h-48 object-cover"
                            initial={{ opacity: 0, y: 50 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: index * 0.1, duration: 0.5 }}
                        />
                        <div className="p-4">
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">{coin.name}</h3>
                        </div>
                    </motion.div>
                ))}
            </motion.div>

            {selectedCoin && (
                <motion.div
                    className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    onClick={handleCoinClose}
                >
                    <motion.div
                        className="bg-white rounded-lg shadow-md overflow-hidden max-w-md mx-auto"
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        exit={{ scale: 0 }}
                        transition={{ duration: 0.3 }}
                    >
                        <img
                            src={selectedCoin.photo_url}
                            alt={`${selectedCoin.name}`}
                            className="w-full h-64 object-cover"
                        />
                        <div className="p-4">
                            <h3 className="text-2xl font-semibold text-gray-800 mb-2">{selectedCoin.name}</h3>
                        </div>
                    </motion.div>
                </motion.div>
            )}
        </>
    );
}

export default App;

