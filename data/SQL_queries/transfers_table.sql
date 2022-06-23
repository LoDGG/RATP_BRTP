CREATE TABLE transfers (
from_stop_id        VARCHAR(64),
to_stop_id          VARCHAR(64),
transfer_type       INT,
min_transfer_time   INT
);
COPY transfers(from_stop_id, to_stop_id, transfer_type, min_transfer_time)
FROM '/home/lod/PycharmProjects/RATP_BRTP/IDFM-gtfs/transfers.csv'
DELIMITER ','
CSV HEADER;

