SELECT from_stop_id,depart.stop_name,depart.location_type as def_type,to_stop_id,arrival.stop_name ,arrival.location_type as arr_type,transfers.min_transfer_time as time 
FROM transfers
LEFT JOIN stops depart ON from_stop_id = depart.stop_id
LEFT JOIN stops arrival ON to_stop_id = arrival.stop_id
where depart.stop_name='Châtelet' and arrival.stop_name!='Châtelet';
