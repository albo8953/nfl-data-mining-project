#!/usr/bin/bash

for g in `cat game_ids`; do
	echo $g
	curl --request GET --url https://api.sportradar.com/nfl/official/trial/v7/en/games/$g/statistics.json --header 'accept: application/json' --header 'x-api-key: LknYs7VGl2IyoHUibBvXLFpZJkX65q2gRRD8eLbZ' > games/$g.json
	sleep 2
done
