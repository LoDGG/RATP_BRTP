CREATE TABLE arrets (
ArRId               INT,
ArRVersion          VARCHAR(64),
ArRCreated          VARCHAR(64),
ArRChanged          VARCHAR(64),
ArRName             VARCHAR(64),
ArRXEpsg2154        INT,
ArRYEpsg2154        INT,
ArRType             VARCHAR(64),
ArRTown             VARCHAR(64),
ArRPostalRegion     INT,
ArRAccessibility    VARCHAR(64),
ArRAudibleSignals   VARCHAR(64),
ArRVisualSigns      VARCHAR(64),
ArRFareZone         VARCHAR(64),
ArRGeopoint         VARCHAR(64)
);
COPY arrets(ArRId,ArRVersion,ArRCreated,ArRChanged,ArRName,ArRXEpsg2154,ArRYEpsg2154,ArRType,ArRTown,ArRPostalRegion,ArRAccessibility,ArRAudibleSignals,ArRVisualSigns,ArRFareZone,ArRGeopoint)
FROM '/home/lod/PycharmProjects/RATP_BRTP/IDFM-gtfs/arrets.csv'
DELIMITER ';'
CSV HEADER;

