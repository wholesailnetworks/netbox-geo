const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy }).setZIndex(0); // Not sure if zindex working 
const map = L.map("map", { layers: [layer], minZoom: 1 });
map.locate()
    .on("locationfound", (e) => map.setView([0,0], 1))
    .on("locationerror", () => map.setView([0, 0], 1));

const markers = JSON.parse(geodata.replace(/&quot;/g,'"'));
async function render_markers() {
    L.geoJSON(markers)
        .bindPopup((layer) => layer.feature.properties.name)
        .addTo(map);
}

map.on("moveend", render_markers);
    []
