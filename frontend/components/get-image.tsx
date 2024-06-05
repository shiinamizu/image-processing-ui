import React, { useState, useEffect} from 'react';
import axios from 'axios';
import { Buffer } from 'buffer';

import {base64Decode} from '@/components/encodingBase64.tsx';

const ImageComponent = () => {
  const [imageData, setImageData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
    const result = await axios.get("http://localhost:8080/api/image",
    {headers:{'Access-Control-Allow-Origin': '*',
    'content-type' : 'image/jpg',
    'responseType' : 'blob'
    }}
      
    );
    const decodedBuff = Buffer.from(result.data["image"], 'base64')
    const file = new File([decodedBuff], 'fileName.jpg', { type: "image/jpg" })
      setImageData(window.URL.createObjectURL(file))

    };

    fetchData();
  }, []);
  console.log(imageData)
  // console.log(imageData)
  return (
    <div>
      {imageData && (
        <img src={imageData} width="500" alt="image1"/>
      )}
    </div>
  );
}

export {ImageComponent};