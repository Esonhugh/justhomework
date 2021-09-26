export url="http://127.0.0.1:5000"
curl "$url/reinitdb"
curl "$url/" -v
sleep 2s
curl "$url/uploadData" -d "user=1&image_url=User1"
curl "$url/uploadData" -d "user=2&image_url=User2"
curl "$url/uploadData" -d "user=3&image_url=User3"
curl "$url/uploadData" -d "user=4&image_url=User4"
curl "$url/uploadData" -d "user=5&image_url=User5"
curl "$url/uploadData" -d "user=6&image_url=User6"
curl "$url/uploadData" -d "user=7&image_url=User7"
curl "$url/uploadData" -d "user=8&image_url=User8"
echo "input user success"
sleep 2s




