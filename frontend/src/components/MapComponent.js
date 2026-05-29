import React, { useEffect, useRef } from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const MapComponent = ({ places }) => {
  const mapRef = useRef(null);
  const mapInstanceRef = useRef(null);
  const markersRef = useRef([]);

  useEffect(() => {
    if (!mapRef.current) return;

    if (!mapInstanceRef.current) {
      mapInstanceRef.current = L.map(mapRef.current).setView([20.5937, 78.9629], 5);

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors",
        maxZoom: 19
      }).addTo(mapInstanceRef.current);
    }

    // Clear previous markers
    markersRef.current.forEach(marker => marker.remove());
    markersRef.current = [];

    if (places && places.length > 0) {
      const map = mapInstanceRef.current;
      const validPlaces = [];

      places.forEach((place, index) => {
        if (place.lat && place.lng) {
          validPlaces.push([place.lat, place.lng]);
          const marker = L.marker([place.lat, place.lng])
            .bindPopup(`<b>${place.name}</b><br/>${place.type}<br/>Hotel: ${place.hotel_name}`)
            .addTo(map);
          markersRef.current.push(marker);
        }
      });

      // Only fit bounds if we have valid coordinates
      if (validPlaces.length > 0) {
        const bounds = L.latLngBounds(validPlaces);
        if (bounds.isValid()) {
          map.fitBounds(bounds, { padding: [50, 50] });
        }
      }
    }
  }, [places]);

  return (
    <div
      ref={mapRef}
      style={{
        height: "500px",
        width: "100%",
        borderRadius: "10px",
        overflow: "hidden",
        border: "2px solid #fff"
      }}
    />
  );
};

export default MapComponent;
