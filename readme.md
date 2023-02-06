## COG Build
sudo cog build
## Docker Run
sudo docker run -d --security-opt seccomp:unconfined -p 3000:5000 cog-script

## Sample Curl
curl --location --request POST 'http://216.153.51.45:3000/predictions' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input": {
        "image": "https://cdn.discordapp.com/attachments/1032842982472290356/1070624613463248906/index.png"
    }
}'