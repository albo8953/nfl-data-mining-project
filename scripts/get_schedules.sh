#!/usr/bin/bash

for s in {2021..2025}; do
	echo $s
	curl --request GET --url https://api.sportradar.com/nfl/official/trial/v7/en/games/$s/REG/schedule.json --header 'accept: application/json' --header 'x-api-key: LknYs7VGl2IyoHUibBvXLFpZJkX65q2gRRD8eLbZ' > ${s}_schedule.json
	sleep 2
done
