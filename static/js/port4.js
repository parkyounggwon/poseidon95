
var osmUrl = "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", // 지도 경로
	osmAttrib = "© <a href='http://openstreetmap.org/copyright'>OpenStreetMap</a> contributors", // 출처
	osm = L.tileLayer(osmUrl, {maxZoom: 18, attribution: osmAttrib}); // 지도 생성시 필요한 기본 옵션

var mymap = L.map('mapid', {
	zoomControl : false, // 지도 줌 컨트롤을 비활성화 시킵니다.
	minZoom: 4, // 지도의 최소 줌 레벨을 설정합니다
	maxZoom: 18 // 지도의 최대 줌 레벨을 설정합니다
}).setView([37.57747387321504,126.98637485504149], 7).addLayer(osm);
