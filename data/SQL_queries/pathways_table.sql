CREATE TABLE PATHWAYS(
    pathway_id              VARCHAR(64),
    from_stop_id            VARCHAR(64),
    to_stop_id              VARCHAR(64),
    pathway_mode            INT,
    is_bidirectional        INT,
    length                  FLOAT,
    traversal_time          INT,
    stair_count             INT,
    max_slope               INT,
    min_width               INT,
    signposted_as           INT,
    reversed_signposted_as  INT
);
COPY pathways(pathway_id,from_stop_id,to_stop_id,pathway_mode,is_bidirectional,
                length,traversal_time,stair_count,max_slope,min_width,
                signposted_as,reversed_signposted_as)
FROM '/home/lod/PycharmProjects/RATP_BRTP/IDFM-gtfs/pathways.csv'
DELIMITER ','
CSV HEADER;
