export url="http://kali.esonhugh.me:8080"
curl "$url/" -v
echo "api usage"
sleep 2s
curl "$url/userdata" -d "user=1&image_url=User1_image"
curl "$url/userdata" -d "user=2&image_url=User2_image"
curl "$url/userdata" -d "user=3&image_url=User3_image"
curl "$url/userdata" -d "user=4&image_url=User4_image"
curl "$url/userdata" -d "user=5&image_url=User5_image"
curl "$url/userdata" -d "user=6&image_url=User6_image"
curl "$url/userdata" -d "user=7&image_url=User7_image"
curl "$url/userdata" -d "user=8&image_url=User8_image"
curl "$url/userdata" -d "user=9&image_url=User9_image"
curl "$url/userdata" -d "user=10&image_url=User10_image"
echo "input user success"
sleep 2s




