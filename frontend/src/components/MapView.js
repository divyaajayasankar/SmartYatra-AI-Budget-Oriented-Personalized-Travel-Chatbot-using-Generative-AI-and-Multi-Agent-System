import React from "react";

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

function MapView({ lat, lng, name }) {

  return (

    <div
      style={{
        height: "400px",
        width: "100%",
        marginTop: "20px",
        borderRadius: "10px",
        overflow: "hidden"
      }}
    >

      <MapContainer
        center={[lat, lng]}

        zoom={14}

        scrollWheelZoom={true}

        style={{
          height: "100%",
          width: "100%"
        }}
      >

        <TileLayer
          attribution='&copy; OpenStreetMap contributors'

          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={[lat, lng]}>

          <Popup>

            <b>{name}</b>

            <br />

            Your selected destination

          </Popup>

        </Marker>

      </MapContainer>

    </div>
  );
}

export default MapView;