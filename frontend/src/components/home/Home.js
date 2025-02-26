import React from "react";
import "./home.css"; // Import CSS

const Home = () => {
  return (
    <div className="home-container">
      
      {/* First Section - AI Chatbot Solution */}
      <div className="chatbot-section">
        <h2>AI Chatbot Solution</h2>
        <button className="start-btn">Get Started</button>
      </div>

      {/* Second Section - Three Blocks */}
      <div className="blocks-section">
        <div className="block">AI-Powerred</div>
        <div className="block">24/7 Avalilable</div>
        <div className="block">Analyitics</div>
      </div>

    </div>
  );
};

export default Home;
