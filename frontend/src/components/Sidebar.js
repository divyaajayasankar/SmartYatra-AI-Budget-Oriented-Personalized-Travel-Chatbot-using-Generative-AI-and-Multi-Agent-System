import React from "react";
import { Link } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {

  return (

    <div className="sidebar">

      <h1 className="logo">
        Travel AI
      </h1>

      <nav className="menu">

        <Link to="/" className="menu-item">
          🏠 Home
        </Link>

        <Link to="/destinations" className="menu-item">
          🗺 Destinations
        </Link>

        <Link to="/budget" className="menu-item">
          💰 Budget
        </Link>

        <Link to="/safety" className="menu-item">
          🛡 Safety
        </Link>

        <Link to="/routes" className="menu-item">
          ✈ Routes
        </Link>

        <Link to="/hotels" className="menu-item">
          🏨 Hotels
        </Link>

        <Link to="/itinerary" className="menu-item">
          📅 Itinerary
        </Link>

      </nav>

    </div>
  );
}

export default Sidebar;