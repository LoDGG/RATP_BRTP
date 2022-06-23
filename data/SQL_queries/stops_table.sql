CREATE TABLE stops (
stop_id         VARCHAR(64),
stop_code       INT,
stop_name       VARCHAR(128),
STOP_DESC       VARCHAR(128),
STOP_LON        FLOAT,
STOP_LAT        FLOAT,
zone_id         INT,
stop_url        INT,
location_type   INT,
parent_station  VARCHAR(64),
stop_timezone   VARCHAR(64),
level_id        INT,
wheelchair_boarding INT,
platform_code   INT
);
COPY stops(stop_id,stop_code,stop_name,stop_desc,stop_lon,stop_lat,zone_id,stop_url,location_type,parent_station,stop_timezone,level_id,wheelchair_boarding,platform_code)
FROM '/home/lod/PycharmProjects/RATP_BRTP/IDFM-gtfs/stops.csv'
DELIMITER ','
CSV HEADER;

