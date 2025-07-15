// Import React and some built-in hooks: useEffect (runs code on component load), useState (manages local state)
import React, { useEffect, useState } from 'react';

function App() {
  // Define a piece of state called `message` with initial value ''
  // `setMessage` is the function used to update this state
  const [message, setMessage] = useState('');

  // useEffect runs once when the component loads (because of the empty [] dependency array)
  useEffect(() => {
    // Fetch data from your FastAPI backend at the root URL ("/")
    fetch('http://127.0.0.1:8000/')
      .then((response) => response.json())       // Parse the JSON from the response
      .then((data) => setMessage(data.message))  // Update the message state with data.message from backend
      .catch((error) => console.error('Error fetching data:', error)); // Log any errors
  }, []);

  return (
    // Render a simple <div> with some inline padding and font style
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      {/* Display the message from the API if loaded, or show "Loading..." as a fallback */}
      <h1>{message || 'Loading...'}</h1>
    </div>
  );
}

// Export this App component so it can be used elsewhere (like in index.js)
export default App;